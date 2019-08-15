import traceback
from  AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.AntZTest.AntsMetaDataConsumer.LoggingAntsMetaDataConsumer import LoggingAntsMetaDataConsumer
class AntsMetaDataConsumerWrapper(BaseAntsMetaDataConsumer):
    def __init__(self,config):
        self.__Consumers=[]
    def AddConsumer(self,consumer:BaseAntsMetaDataConsumer):
        self.__Consumers.append(consumer)
    def ProcessPreRun(self,numberofsteps, maze, aditionaldata):
        try:
            for consumer in self.__Consumers:
                consumer.ProcessPreRun(numberofsteps, maze, aditionaldata)
        except Exception:
            traceback.print_exc()



    def ProcessPreSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        try:
            for consumer in self.__Consumers:
                consumer.ProcessPreSysStep(step, worldimage, aditionaldata)
        except Exception:
            traceback.print_exc()

    def ProcessAntStep(self,step, ant:BasicAnt,antworldimage:BaseSingleAntWorldImage,move,  aditionaldata):
        try:
            for consumer in self.__Consumers:
                consumer.ProcessAntStep(step, ant,antworldimage,move,  aditionaldata)
        except Exception:
            traceback.print_exc()

    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        try:
            for consumer in self.__Consumers:
                consumer.ProcessPostSysStep(step, worldimage, aditionaldata)
        except Exception:
            traceback.print_exc()

    def ProcessPreStopRun(self,numberofsteps, worldimage:BaseTotalWorldImage, aditionaldata):
        try:
            for consumer in self.__Consumers:
                consumer.ProcessPreStopRun(numberofsteps, worldimage, aditionaldata)
        except Exception:
            traceback.print_exc()