import traceback
from  AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.AntZTest.AntsMetaDataConsumer.LoggingAntsMetaDataConsumer import LoggingAntsMetaDataConsumer
class AntsMetaDataConsumerWrapper(BaseAntsMetaDataConsumer):
    def __init__(self,config):
        # TODO add DILL Serialization
        # TODO add Messege to web
        self.__Consumers=[LoggingAntsMetaDataConsumer(config)]

    def ProcessPreRun(self,numberofsteps, maze, aditionaldata):
        try:
            for consumer in self.__Consumers:
                self.__Consumers.ProcessPreRun(numberofsteps, maze, aditionaldata)
        except Exception:
            traceback.print_exc()



    def ProcessPreSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        try:
            for consumer in self.__Consumers:
                consumer.ProcessPreRun(step, worldimage, aditionaldata)
        except Exception:
            traceback.print_exc()

    def ProcessAntStep(self,step, ant,antworldimage:BaseSingleAntWorldImage,move,  aditionaldata):
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