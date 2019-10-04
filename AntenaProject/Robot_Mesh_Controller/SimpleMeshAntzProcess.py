
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
from AntenaProject.Common.Maze.Parsers.DIYMazeParser import DIYMazeParser
from AntenaProject.Robot_Mesh_Controller.SimpleMeshAntProducer import SimpleMeshAntProducer

from AntenaProject.Robot_Mesh_Controller.MeshWorldImageProvider import MeshWorldImageProvider
from AntenaProject.Common.Config.IniConfigProvider import IniConfigProvider
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.Common.PerfromanceCounting.LoggerPerofromanceWriter import LoggerPerofromanceWriter
from AntenaProject.Common.PerfromanceCounting.DillPerofromanceWriter import DillPerofromanceWriter
from AntenaProject.AntZTest.AntsMetaDataConsumer.AntsMetaDataConsumerWrapper import AntsMetaDataConsumerWrapper
from AntenaProject.AntZTest.AntsMetaDataConsumer.LoggingAntsMetaDataConsumer import LoggingAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.DillAntsMetaDataConsumer import  DillAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.DrawingMetaDataConsumer import DrawingMetaDataConsumer
from AntenaProject.AntZTest.AntsRunEvaluation.ComposedEvaluationResponse import ComposedEvaluationResponse
from AntenaProject.SimpleExample.SimpleAntEvaluator import SimpleAntEvaluator
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
from AntenaProject.AntZTest.AntsRunEvaluation.EvaluationResponseWrapper import EvaluationResponseWrapper
from AntenaProject.AntZTest.AntsMetaDataConsumer.MetrySenderMetaDataConsumer import MetrySenderMetaDataConsumer
from AntenaProject.AntZTest.Commands.CommandsReciver import CommandsReciver
from AntenaProject.AntZTest.AntsController.TimedStepEnabler import TimedStepEnabler
from AntenaProject.AntZTest.AntsMetaDataConsumer.DummyMetaDataToNodeStateInterperter import DummyMetaDataToNodeStateInterperter
from AntenaProject.AntZTest.RobotCommuincation.ServerComm import ServerComm
from AntenaProject.AntZTest.RobotCommuincation.RobotMetadataConsumer import RobotMetadataConsumer
from AntenaProject.AntZTest.StepCounter.AntStepProcesser import AntStepProcesser
from AntenaProject.MeshAnts.connectivty_calculator import connectivty_calculator
from typing import List,Tuple
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Robot_Mesh_Controller.SimpleMeshAntsController import SimpleMeshAntsContrller
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
    #parser=DIYMazeParser(5)
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
    metadataconsumer.AddConsumer(DrawingMetaDataConsumer(config,CreateFolder(configprovider,baseTestFolder,"Drawing_Maze"),maze.GetEnterence()))
    metadataconsumer.AddConsumer(MetrySenderMetaDataConsumer(config,DummyMetaDataToNodeStateInterperter()))
    metadataconsumer.AddConsumer(DillAntsMetaDataConsumer(config,CreateFolder(configprovider,baseTestFolder,"Data")))
    performancecounterwritter=PerofromanceWriterWrapper(configprovider)
    performancecounterwritter.AddWritter(LoggerPerofromanceWriter(configprovider))
    performancecounterwritter.AddWritter(DillPerofromanceWriter(configprovider,CreateFolder(configprovider,baseTestFolder,"Performance")))
    evaluationWrapper=EvaluationResponseWrapper(configprovider)
    evaluationWrapper.AddEvaluator(SimpleAntEvaluator(configprovider))
    step_enabler=TimedStepEnabler(int(configprovider.GetConfigValueForSectionAndKey("RunDefinations","SecondsPerStep",5)))
    commandreciver= CommandsReciver(configprovider)
    commandreciver.Start()
    connectivty=connectivty_calculator(config=configprovider,maze_facade=maze)
    return  SimpleMeshAntsContrller(config,
                                maze,
                                metadataconsumer,
                                performancecounterwritter,
                                MeshWorldImageProvider(config,maze,commandreciver),
                                SimpleMeshAntProducer(configprovider,maze.GetEnterence(),maze=maze,connectivty_calculator=connectivty,number_to_produce=6),
                                evaluationWrapper,connectivty)


if __name__ == '__main__':
    config=GetConfig()
    baseTestFolder=format(f"Test_{time.time()}")
    CreatLogger(config,baseTestFolder)
    maze=GetMaze(config)
    testController=GetAntsController(config,maze,baseTestFolder)
    result=testController.Process()


    #genrate AA Report (time....)




