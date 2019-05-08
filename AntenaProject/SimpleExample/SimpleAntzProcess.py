from typing import List,Tuple
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.SimpleExample.SimpleAntsController import SimpleAntsContrller
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
from AntenaProject.SimpleExample.SimpleAntProducer import SimpleAntProducer
from AntenaProject.SimpleExample.SimpleWorldImageProvider import SimpleWorldImageProvider
from AntenaProject.Common.Config.IniConfigProvider import IniConfigProvider
import logging
from typing import List

import os
#Out main file

def GetConfig()->BaseConfigProvider:
    filename=os.path.join(os.path.dirname(__file__),"Config.ini")
    configprovider=IniConfigProvider(filename)
    return configprovider
def GetMaze(configprovider:BaseConfigProvider)->MazeFacade:
    filename = configprovider.GetConfigValueForSectionAndKey('MAZE', 'filename')
    filename = os.path.join(os.path.dirname(__file__), filename)
    parser = FileMazeParser(filename)
    return MazeFacade(parser)
def CreatLogger(configprovider:BaseConfigProvider):
   logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')


def GetAntsController(configprovider,maze):
    return  SimpleAntsContrller(config,maze,SimpleWorldImageProvider(config,maze),SimpleAntProducer(configprovider,maze.GetEnterence()))


if __name__ == '__main__':
    config=GetConfig()
    CreatLogger(config)
    maze=GetMaze(config)
    testController=GetAntsController(config,maze)
    testController.Process()
    #genrate AA Report (time....)




