from AntenaProject.AntZTest.MultiRun.BaseMultiRunAgent import BaseMultiRunAgent
from typing import List,Tuple
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.SimpleExample.SimpleAntsController import SimpleAntsContrller
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
from AntenaProject.Common.Maze.Parsers.DIYMazeParser import DIYMazeParser
from AntenaProject.SimpleExample.SimpleAntProducer import SimpleAntProducer
from AntenaProject.SimpleExample.SimpleWorldImageProvider import SimpleWorldImageProvider
from AntenaProject.Common.Config.IniConfigProvider import IniConfigProvider
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.Common.PerfromanceCounting.LoggerPerofromanceWriter import LoggerPerofromanceWriter
from AntenaProject.Common.PerfromanceCounting.DillPerofromanceWriter import DillPerofromanceWriter
from AntenaProject.AntZTest.AntsMetaDataConsumer.AntsMetaDataConsumerWrapper import AntsMetaDataConsumerWrapper
from AntenaProject.AntZTest.AntsMetaDataConsumer.LoggingAntsMetaDataConsumer import LoggingAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.DillAntsMetaDataConsumer import  DillAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.SummeryMetaDataConsumer import  SummeryMetaDataConsumer

from AntenaProject.AntZTest.AntsMetaDataConsumer.DrawingMetaDataConsumer import DrawingMetaDataConsumer

import logging
import time
from typing import List
import sys
import os
#Out main file
class SimpleMultiAntzAgent(BaseMultiRunAgent):

    def __init__(self,id,config:BaseConfigProvider,maze:MazeFacade,basefolder,return_dict):
        BaseMultiRunAgent.__init__(self,id,config,maze,return_dict)
        self._basicrunfolder=os.path.join(basefolder,str(id))
        self._SummeryMetaDataConsumer=SummeryMetaDataConsumer(config)

    def _InternalStart(self):
        baseTestFolder = format(f"Test_{self._id}_{time.time()}")

        self.CreatLogger(self._config)

        self._testController = self.GetAntsController(self._config, self._Maze)



    def _InternalProcess(self):
        self._testController.Process()

    def _ComposeResult(self) -> str:
        return  self._SummeryMetaDataConsumer.GetSummery()

    def _InternalStop(self):
        pass

    def _InternalTermination(self):
        pass

    def GetAntsController(self,configprovider, maze):
        metadataconsumer = AntsMetaDataConsumerWrapper(configprovider)
        metadataconsumer.AddConsumer(LoggingAntsMetaDataConsumer(configprovider))
        metadataconsumer.AddConsumer( self._SummeryMetaDataConsumer)
        #metadataconsumer.AddConsumer(DrawingMetaDataConsumer(configprovider))
        metadataconsumer.AddConsumer(
            DillAntsMetaDataConsumer(configprovider, self.CreateFolder(self._basicrunfolder, "Data")))
        performancecounterwritter = PerofromanceWriterWrapper(configprovider)
        performancecounterwritter.AddWritter(LoggerPerofromanceWriter(configprovider))
        performancecounterwritter.AddWritter(
            DillPerofromanceWriter(configprovider, self.CreateFolder(self._basicrunfolder, "Performance")))

        return SimpleAntsContrller(configprovider, maze, metadataconsumer, performancecounterwritter
                                   , SimpleWorldImageProvider(configprovider, maze),
                                   SimpleAntProducer(configprovider, maze.GetEnterence()))

    def CreateFolder(self,basicrunfolder, subfolder):
        newpath = os.path.join(basicrunfolder,  subfolder)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            return newpath
        return None

    def GetMaze(configprovider: BaseConfigProvider) -> MazeFacade:
        filename = configprovider.GetConfigValueForSectionAndKey('MAZE', 'filename')
        filename = os.path.join(os.path.dirname(__file__), filename)
        parser = FileMazeParser(filename)
        # parser=DIYMazeParser(5)
        return MazeFacade(parser)

    def CreatLogger(self,configprovider: BaseConfigProvider):
        folder = self.CreateFolder(self._basicrunfolder, "Log")
        if folder is not None:
            logfilename = os.path.join(folder, 'log.txt')
            # set up logging to file - see previous section for more details
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                datefmt='%m-%d %H:%M',
                                filename=logfilename,
                                filemode='w')
            # define a Handler which writes INFO messages or higher to the sys.stderr
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            # set a format which is simpler for console use
            formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
            # tell the handler to use this format
            console.setFormatter(formatter)
            # add the handler to the root logger
            logging.getLogger('').addHandler(console)