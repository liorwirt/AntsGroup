from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.AntZTest.AntsMetaDataConsumer.AntsMetaDataConsumerWrapper import AntsMetaDataConsumerWrapper
from AntenaProject.Common.PerfromanceCounting.PerformanceCounter import PerformanceCounter
from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from abc import ABC,abstractmethod
from typing import Dict
import sys
import logging

def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

class BaseAntsController(ABC):
    def __init__(self,config,maze,basicWorldImageProvider:BasicWorldImageProvider,antsproducer:BasicAntProducer):
        sys.excepthook = handle_exception
        self._PerformanceWritterWrapper=PerofromanceWriterWrapper()
        self._Maze=maze
        self._basicWorldImageProvider=basicWorldImageProvider
        self._Config=config
        self._AntsMetaDataConsumer=AntsMetaDataConsumerWrapper(config)
        self._NumberOfSteps=self.__Config.GetConfigValueForSectionAndKey('RunDefinations','NumberOfSteps',200)
        self._Ants=antsproducer
        self._Ants.CreateAnts()
    def Process(self):
        with PerformanceCounter("Process",self._PerformanceWritterWrapper):

            self.__AntsMetaDataConsumer.ProcessPreRun(self.__NumberOfSteps,self.__Maze,self._GetPreTestAdditionalData())
            counter=0

            while counter<self.__NumberOfSteps:
                with PerformanceCounter("Colony_Step", self._PerformanceWritterWrapper):
                    counter+=1
                    self._AntsMetaDataConsumer.ProcessPreSysStep(counter,self._basicWorldImageProvider.GetAntWorldImage(),self._GetPrePreStepAdditionalData())
                    for ant in self.__Ants:
                        with PerformanceCounter(format(f"Ant_{ant.ID} step"), self._PerformanceWritterWrapper):
                            antworldimage=self._basicWorldImageProvider.GetAntWorldImage()
                            step=ant.GetStep(antworldimage)
                            self._AntsMetaDataConsumer.ProcessAntStep(counter,ant,antworldimage,step,None)
                    for ant in self.__Ants:
                        ant.UpdatePosition(self._basicWorldImageProvider.GetAntPosition(ant))
                    self._AntsMetaDataConsumer.ProcessPostSysStep(counter, self._basicWorldImageProvider.GetAntWorldImage(), self._GetPostStepAdditionalData())

            self._AntsMetaDataConsumer.ProcessPreStopRun(self.__NumberOfSteps, self.__Maze, self._GetPostTestAdditionalData())
    @abstractmethod
    def _GetPreTestAdditionalData(self)->Dict:
        pass

    @abstractmethod
    def _GetPrePreStepAdditionalData(self) -> Dict:
        pass

    @abstractmethod
    def _GetPostStepAdditionalData(self) -> Dict:
        pass

    @abstractmethod
    def _GetPostTestAdditionalData(self) -> Dict:
        pass