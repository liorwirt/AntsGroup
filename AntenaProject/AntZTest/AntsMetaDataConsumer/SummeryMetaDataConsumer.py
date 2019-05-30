
from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
import logging
from pprint import pformat
class SummeryMetaDataConsumer(BaseAntsMetaDataConsumer):
    def __init__(self,config):
        BaseAntsMetaDataConsumer.__init__(self,config)
        self._Summery=''

    def ProcessPreRun(self,numberofsteps,maze,aditionaldata):
      pass

    def ProcessPreSysStep(self,step,worldimage:BaseTotalWorldImage, aditionaldata):
        pass
    def ProcessAntStep(self,step,ant:BasicAnt,antworldimage,move,aditionaldata):
        pass
    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        pass
    def ProcessPreStopRun(self,numberofsteps,worldimage:BaseTotalWorldImage , aditionaldata):
        self._Summery=format(f"pre end run on maze coverage {worldimage.Coverage} for {numberofsteps} steps aditionaldata:{pformat(aditionaldata)}")
    def GetSummery(self):
        return self._Summery
