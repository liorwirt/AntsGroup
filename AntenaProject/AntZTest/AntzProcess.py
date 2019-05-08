from typing import List,Tuple
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.AntZTest.AntsController.BaseAntsController import BaseAntsController
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
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
    return MazeFacade(filename)
def CreatLogger(configprovider:BaseConfigProvider):
   logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')


def GetAntsController(configprovider,maze):
    #TODO add missing dependencies
    return  BaseAntsController(configprovider,maze)


if __name__ == '__main__':
    config=GetConfig()
    CreatLogger(config)
    maze=GetMaze(config)
    testController=GetAntsController(config,maze)
    testController.Process()
    #genrate AA Report (time....)




