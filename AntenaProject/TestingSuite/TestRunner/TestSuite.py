from typing import List,Tuple
from AntenaProject.TestingSuite.TestRunner.TestProcess.ICD.TestServiceStatus import TestServiceStatus
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.TestingSuite.TestRunner.TestController import TestController
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
#Out main file

def GetConfig()->BaseConfigProvider:
    pass
def GetMaze(configprovider:BaseConfigProvider)->MazeFacade:
    pass
def CreatLogger(configprovider:BaseConfigProvider):
    pass
def GetTesController(configprovider)->TestController:
    #returns all the configurations for our tests
    pass
def DisplayData(testsdata:list[TestServiceStatus]):
    #print data
    pass

if __name__ == '__main__':
    config=GetConfig()
    CreatLogger(config)
    maze=GetMaze(config)
    testController=GetTesController(config,maze)
    testController.Start()
    while(not testController.AreTestsFinished):
        DisplayData(testController.ReportStatus())




