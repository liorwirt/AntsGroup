from typing import List, Tuple
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.SimpleExample.SimpleAntsController import SimpleAntsContrller
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
from AntenaProject.AlgoAnt.AlgoExample.RobotAlgoAntProducer import RobotAlgoAntProducer
from AntenaProject.AlgoAnt.WorldImage.UnifiedWorldImageProvider import UnifiedWorldImageProvider
from AntenaProject.Common.Config.IniConfigProvider import IniConfigProvider
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.Common.PerfromanceCounting.LoggerPerofromanceWriter import LoggerPerofromanceWriter
from AntenaProject.Common.PerfromanceCounting.DillPerofromanceWriter import DillPerofromanceWriter
from AntenaProject.AntZTest.AntsMetaDataConsumer.AntsMetaDataConsumerWrapper import AntsMetaDataConsumerWrapper
from AntenaProject.AntZTest.AntsMetaDataConsumer.LoggingAntsMetaDataConsumer import LoggingAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.DillAntsMetaDataConsumer import DillAntsMetaDataConsumer
from AntenaProject.AlgoAnt.AlgoExample.AlgoAntDrawingMetaDataConsumer import AlgoAntDrawingMetaDataConsumer
from AntenaProject.AntZTest.AntsRunEvaluation.EvaluationResponseWrapper import EvaluationResponseWrapper
from AntenaProject.SimpleExample.SimpleAntEvaluator import SimpleAntEvaluator
from AntenaProject.AntZTest.Commands.CommandsReciver import CommandsReciver
from AntenaProject.AntZTest.AntsMetaDataConsumer.MetrySenderMetaDataConsumer import MetrySenderMetaDataConsumer
from AntenaProject.AlgoAnt.AlgoExample.AlgoAntMetaDataToNodeStateInterperter import \
    AlgoAntMetaDataToNodeStateInterperter
from AntenaProject.AntZTest.RobotCommuincation.ServerComm import ServerComm
from AntenaProject.AntZTest.RobotCommuincation.RobotMetadataConsumer import RobotMetadataConsumer
from AntenaProject.AntZTest.StepCounter.AntStepProcesser import AntStepProcesser

import logging
import time
from typing import List
import sys
import os


# Out main file

def GetConfig() -> BaseConfigProvider:
    filename = os.path.join(os.path.dirname(__file__), "Config.ini")
    configprovider = IniConfigProvider(filename)
    return configprovider


def CreateFolder(configprovider: BaseConfigProvider, basename, subfolder):
    basicrunfolder = configprovider.GetConfigValueForSectionAndKey('Data', 'BaseFolder')
    newpath = os.path.join(basicrunfolder, os.path.join(basename, subfolder))
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


def CreatLogger(configprovider: BaseConfigProvider, testfolder):
    folder = CreateFolder(configprovider, testfolder, "Log")
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


def GetAntsController(configprovider, maze, baseTestFolder):

    metadataconsumer = AntsMetaDataConsumerWrapper(configprovider)
    server_comm = ServerComm(configprovider)
    ant_step_processer = AntStepProcesser(configprovider)
   # metadataconsumer.AddConsumer(RobotMetadataConsumer(configprovider, server_comm, ant_step_processer))
    metadataconsumer.AddConsumer(LoggingAntsMetaDataConsumer(configprovider))
    metadataconsumer.AddConsumer(MetrySenderMetaDataConsumer(configprovider, AlgoAntMetaDataToNodeStateInterperter()))
    metadataconsumer.AddConsumer(AlgoAntDrawingMetaDataConsumer(configprovider))
    metadataconsumer.AddConsumer(DillAntsMetaDataConsumer(configprovider, CreateFolder(configprovider, baseTestFolder, "Data")))
    performancecounterwritter = PerofromanceWriterWrapper(configprovider)
    performancecounterwritter.AddWritter(LoggerPerofromanceWriter(configprovider))
    performancecounterwritter.AddWritter(
        DillPerofromanceWriter(configprovider, CreateFolder(configprovider, baseTestFolder, "Performance")))
    evaluationWrapper = EvaluationResponseWrapper(configprovider)
    evaluationWrapper.AddEvaluator(SimpleAntEvaluator(configprovider))
    commandreciver = CommandsReciver(configprovider)
    commandreciver.Start()
    return SimpleAntsContrller(configprovider, maze, metadataconsumer, performancecounterwritter,
                               UnifiedWorldImageProvider(configprovider, maze, commandreciver),
                               RobotAlgoAntProducer(configprovider, ant_step_processer.initial_position(),server_comm=server_comm),
                               evaluationWrapper)


if __name__ == '__main__':
    config = GetConfig()
    baseTestFolder = format(f"Test_{time.time()}")
    CreatLogger(config, baseTestFolder)
    maze = GetMaze(config)
    testController = GetAntsController(config, maze, baseTestFolder)
    testController.Process()
    # genrate AA Report (time....)
