from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.Common.PerfromanceCounting.PerformanceCounter import PerformanceCounter
from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from abc import ABC,abstractmethod
from typing import Dict
import sys
import logging
from AntenaProject.AntZTest.AntsMetaDataConsumer.AntsMetaDataConsumerWrapper import AntsMetaDataConsumerWrapper
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

class BaseAntsController(ABC):
    def __init__(self,config,maze,metadataconsumer:AntsMetaDataConsumerWrapper,performanceCounterWrapper:PerofromanceWriterWrapper,basicWorldImageProvider:BasicWorldImageProvider,antsproducer:BasicAntProducer):
        sys.excepthook = handle_exception
        self._PerformanceWritterWrapper=performanceCounterWrapper
        self._Maze=maze
        self._WorldImageProvider=basicWorldImageProvider
        self._Config=config
        self._AntsMetaDataConsumer=metadataconsumer
        self._NumberOfSteps=int(self._Config.GetConfigValueForSectionAndKey('RunDefinations','NumberOfSteps',200))
        self._Ants=antsproducer
        self._Ants.CreateAnts()
    def Process(self):
        with PerformanceCounter("Process",self._PerformanceWritterWrapper):

            self._AntsMetaDataConsumer.ProcessPreRun(self._NumberOfSteps,self._Maze,self._GetPreTestAdditionalData())
            counter=0

            while counter<self._NumberOfSteps:
                with PerformanceCounter("Colony_Step", self._PerformanceWritterWrapper):
                    counter+=1
                    self._AntsMetaDataConsumer.ProcessPreSysStep(counter,
                                                                 self._WorldImageProvider.GetWorldImage(),
                                                                 self._GetPrePreStepAdditionalData())
                    for ant in self._Ants:
                        with PerformanceCounter(format(f"Ant_{ant.ID} step"), self._PerformanceWritterWrapper):
                            antworldimage=self._WorldImageProvider.GetAntWorldImage(ant)
                            step=ant.GetStep(antworldimage)
                            self._WorldImageProvider.ProcessStep(ant, step)
                            self._AntsMetaDataConsumer.ProcessAntStep(counter,ant,antworldimage,step,None)
                    self._WorldImageProvider.UpdatePositionsAccordingToMoves()
                    self._AntsMetaDataConsumer.ProcessPostSysStep(counter, self._WorldImageProvider.GetWorldImage(), self._GetPostStepAdditionalData())

            self._AntsMetaDataConsumer.ProcessPreStopRun(self._NumberOfSteps, self._WorldImageProvider.GetWorldImage(), self._GetPostTestAdditionalData())
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