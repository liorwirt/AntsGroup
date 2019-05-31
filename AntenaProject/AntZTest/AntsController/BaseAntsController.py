from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.Common.PerfromanceCounting.PerformanceCounter import PerformanceCounter
from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
from abc import ABC,abstractmethod
from typing import Dict
import sys
import logging
from AntenaProject.AntZTest.AntsMetaDataConsumer.AntsMetaDataConsumerWrapper import AntsMetaDataConsumerWrapper
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.AntZTest.AntsRunEvaluation.EvaluationResponseWrapper import EvaluationResponseWrapper
from AntenaProject.AntZTest.AntsRunEvaluation.BaseEvaluationResponse import BaseEvaluationResponse
from AntenaProject.AntZTest.AntsRunEvaluation.ComposedEvaluationResponse import ComposedEvaluationResponse
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    return ComposedEvaluationResponse.GetExceptionResult(format(f"exc_type: {exc_type} exc_value:{exc_value} exc_traceback:{exc_traceback}"))

class BaseAntsController(ABC):
    def __init__(self,config,maze,metadataconsumer:AntsMetaDataConsumerWrapper,performanceCounterWrapper:PerofromanceWriterWrapper,basicWorldImageProvider:BasicWorldImageProvider,antsproducer:BasicAntProducer,evaulationWrapper:EvaluationResponseWrapper):
        sys.excepthook = handle_exception
        self._PerformanceWritterWrapper=performanceCounterWrapper
        self._Maze=maze
        self._WorldImageProvider=basicWorldImageProvider
        self._Config=config
        self._AntsMetaDataConsumer=metadataconsumer
        self._NumberOfSteps=int(self._Config.GetConfigValueForSectionAndKey('RunDefinations','NumberOfSteps',200))
        self._Ants=antsproducer
        self._Ants.CreateAnts()
        self._EvaulationWrapper=evaulationWrapper
    def Process(self)->ComposedEvaluationResponse:
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
                            step,antAdditionalData=ant.GetStep(antworldimage)
                            self._WorldImageProvider.ProcessStep(ant, step)
                            self._AntsMetaDataConsumer.ProcessAntStep(counter,ant,antworldimage,step,antAdditionalData)
                            response=self._EvaulationWrapper.EvalAntStep(ant,antworldimage,step,antAdditionalData)
                            if not self._MayContinueAfterEvalAntStep(response):
                                return response

                    self._WorldImageProvider.UpdatePositionsAccordingToMoves()
                    self._AntsMetaDataConsumer.ProcessPostSysStep(counter, self._WorldImageProvider.GetWorldImage(), self._GetPostStepAdditionalData())
                    response=self._EvaulationWrapper.EvalWorldState(self._WorldImageProvider.GetWorldImage(), self._GetPostStepAdditionalData())
                    if not self._MayContinueAfterEvalWorldState(response):
                        return response


            self._AntsMetaDataConsumer.ProcessPreStopRun(self._NumberOfSteps, self._WorldImageProvider.GetWorldImage(), self._GetPostTestAdditionalData())
            response=ComposedEvaluationResponse.GetOkResult();
            return response;
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

    @abstractmethod
    def _MayContinueAfterEvalWorldState(self,response:ComposedEvaluationResponse) -> bool:
        pass

    @abstractmethod
    def _MayContinueAfterEvalWorldState(self, response:ComposedEvaluationResponse) -> bool:
        pass

    @abstractmethod
    def _MayContinueAfterEvalAntStep(self, response) -> bool:
        pass
