
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.FileMazeParser import FileMazeParser
import numpy as np
from AntenaProject.Common.Config.IniConfigProvider import IniConfigProvider
from multiprocessing import Process
from AntenaProject.SimpleExample.MultiRun.SimpleMultiAntzAgent import SimpleMultiAntzAgent
import time
from AntenaProject.SimpleExample.MultiRun.MultiRunReportWriter import MultiRunReportWriter
import multiprocessing

import os

def GetConfig()->BaseConfigProvider:
    filename=os.path.join(os.path.dirname(__file__),"Config.ini")
    configprovider=IniConfigProvider(filename)
    return configprovider
def CreateFolder(configprovider:BaseConfigProvider,basename):
    basicrunfolder=configprovider.GetConfigValueForSectionAndKey('Data', 'BaseFolder')
    newpath=os.path.join(basicrunfolder,basename)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        return newpath
    return None
def GetMaze(configprovider:BaseConfigProvider)->MazeFacade:
    filename = configprovider.GetConfigValueForSectionAndKey('MAZE', 'filename')
    filename = os.path.join(os.path.dirname(__file__), filename)
    parser = FileMazeParser(filename)
    return MazeFacade(parser)
def CreateProcess(configprovider,maze:MazeFacade,basefolder,numberOfProcess,visibilityRange,repoertwriter,return_dict):
    ListOftProcess=[]

    for i in range(numberOfProcess):
        visibility = np.random.randint(visibilityRange[0], visibilityRange[1])
        configprovider.SetConfigSection('SimpleAnt', 'VisibilityRange', str(visibility))
        configprovider.SetConfigSection('SimpleAnt', 'AllowedMovement', str(visibility))
        repoertwriter.SetDataForProcess(i,format(f"VisibilityRange = {visibility} AllowedMovement={visibility}"))
        ListOftProcess.append( SimpleMultiAntzAgent(i,configprovider,maze,basefolder,return_dict))
    return ListOftProcess

if __name__ == '__main__':
    config=GetConfig()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    baseTestFolder=CreateFolder(config,format(f"MultiTest_{time.time()}"))
    repoertwriter = MultiRunReportWriter(baseTestFolder)
    maze=GetMaze(config)
    numberOfProcess=10
    visibilityRange=(1,10)
    ListOftProcess=CreateProcess(config,maze,baseTestFolder,numberOfProcess,visibilityRange,repoertwriter,return_dict)

    for process in ListOftProcess:
        process.start()
        time.sleep(2)
    for process in ListOftProcess:
        process.join()
    for key in return_dict.keys():
        repoertwriter.SetResultForProcess(key,return_dict[key])
    repoertwriter.ComposeReport()





