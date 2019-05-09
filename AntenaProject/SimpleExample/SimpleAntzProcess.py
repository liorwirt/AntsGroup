from typing import List,Tuple
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.SimpleExample.SimpleAntsController import SimpleAntsContrller
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
from AntenaProject.SimpleExample.SimpleAntProducer import SimpleAntProducer
from AntenaProject.SimpleExample.SimpleWorldImageProvider import SimpleWorldImageProvider
from AntenaProject.Common.Config.IniConfigProvider import IniConfigProvider
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.Common.PerfromanceCounting.LoggerPerofromanceWriter import LoggerPerofromanceWriter
from AntenaProject.Common.PerfromanceCounting.DillPerofromanceWriter import DillPerofromanceWriter
from AntenaProject.AntZTest.AntsMetaDataConsumer.AntsMetaDataConsumerWrapper import AntsMetaDataConsumerWrapper
from AntenaProject.AntZTest.AntsMetaDataConsumer.LoggingAntsMetaDataConsumer import LoggingAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.DillAntsMetaDataConsumer import  DillAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.DrawingMetaDataConsumer import DrawingMetaDataConsumer

import logging
import time
from typing import List
import sys
import os
#Out main file

def GetConfig()->BaseConfigProvider:
    filename=os.path.join(os.path.dirname(__file__),"Config.ini")
    configprovider=IniConfigProvider(filename)
    return configprovider
def CreateFolder(configprovider:BaseConfigProvider,basename,subfolder):
    basicrunfolder=configprovider.GetConfigValueForSectionAndKey('Data', 'BaseFolder')
    newpath=os.path.join(basicrunfolder,os.path.join(basename,subfolder))
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        return newpath
    return None
def GetMaze(configprovider:BaseConfigProvider)->MazeFacade:
    filename = configprovider.GetConfigValueForSectionAndKey('MAZE', 'filename')
    filename = os.path.join(os.path.dirname(__file__), filename)
    parser = FileMazeParser(filename)
    return MazeFacade(parser)
def CreatLogger(configprovider:BaseConfigProvider,testfolder):
   folder=CreateFolder(configprovider,testfolder,"Log")
   if folder is not None:
       logfilename=os.path.join(folder,'log.txt')
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

def GetAntsController(configprovider,maze,baseTestFolder):
    metadataconsumer=AntsMetaDataConsumerWrapper(configprovider)
    metadataconsumer.AddConsumer(LoggingAntsMetaDataConsumer(config))
    metadataconsumer.AddConsumer(DrawingMetaDataConsumer(config))
    metadataconsumer.AddConsumer(DillAntsMetaDataConsumer(config,CreateFolder(configprovider,baseTestFolder,"Data")))
    performancecounterwritter=PerofromanceWriterWrapper(configprovider)
    performancecounterwritter.AddWritter(LoggerPerofromanceWriter(configprovider))
    performancecounterwritter.AddWritter(DillPerofromanceWriter(configprovider,CreateFolder(configprovider,baseTestFolder,"Performance")))

    return  SimpleAntsContrller(config,maze,metadataconsumer,performancecounterwritter
                                ,SimpleWorldImageProvider(config,maze),SimpleAntProducer(configprovider,maze.GetEnterence()))


if __name__ == '__main__':
    config=GetConfig()
    baseTestFolder=format(f"Test_{time.time()}")
    CreatLogger(config,baseTestFolder)
    maze=GetMaze(config)
    testController=GetAntsController(config,maze,baseTestFolder)
    testController.Process()
    #genrate AA Report (time....)




