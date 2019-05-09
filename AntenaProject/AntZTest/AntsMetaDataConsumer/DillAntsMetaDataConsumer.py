from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
import dill
import os
class DillAntsMetaDataConsumer(BaseAntsMetaDataConsumer):
    def __init__(self,config,targetfolder):
        BaseAntsMetaDataConsumer.__init__(self,config)
        self._ProcessPreRunFile=os.path.join(targetfolder,"ProcessPreRun.dill")
        self._ProcessPreSysStepFile = os.path.join(targetfolder, "ProcessPreSysStep.dill")
        self._ProcessAntStepFile = os.path.join(targetfolder, "ProcessAntStep.dill")
        self._ProcessPostSysStepFile = os.path.join(targetfolder, "ProcessPostSysStep.dill")
        self._ProcessPreStopRunFile = os.path.join(targetfolder, "ProcessPreStopRun.dill")
    def ProcessPreRun(self,numberofsteps,maze,aditionaldata):
        self.__WrtieTofile([numberofsteps, maze, aditionaldata], self._ProcessPreRunFile)
    def ProcessPreSysStep(self,step,worldimage:BaseTotalWorldImage, aditionaldata):
        self.__WrtieTofile([step, worldimage, aditionaldata],self._ProcessPreSysStepFile)
    def ProcessAntStep(self,step,ant:BasicAnt,antworldimage,move,aditionaldata):
        self.__WrtieTofile([step, ant,antworldimage, aditionaldata], self._ProcessAntStepFile)
    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        self.__WrtieTofile([step, worldimage, aditionaldata],self._ProcessPostSysStepFile)
    def ProcessPreStopRun(self,numberofsteps,worldimage:BaseTotalWorldImage , aditionaldata):
        self.__WrtieTofile([numberofsteps, worldimage, aditionaldata],self._ProcessPreStopRunFile)

    def __WrtieTofile(self,data,filename):
        with open(filename, "ab") as dill_file:
            dill.dump(data, dill_file)