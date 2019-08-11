from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.Common.PerfromanceCounting.PerformanceWritterWrapper import PerofromanceWriterWrapper
from AntenaProject.Common.PerfromanceCounting.PerformanceCounter import PerformanceCounter
from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
from abc import ABC, abstractmethod
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
    def __init__(self, config, maze, metadataconsumer: AntsMetaDataConsumerWrapper,
                 performanceCounterWrapper: PerofromanceWriterWrapper, basicWorldImageProvider: BasicWorldImageProvider,
                 antsproducer: BasicAntProducer, evaulationWrapper:EvaluationResponseWrapper):
        sys.excepthook = handle_exception
        self._performance_writter_wrapper = performanceCounterWrapper
        self._Maze = maze
        self._world_image_provider = basicWorldImageProvider
        self._Config = config
        self._ants_meta_data_consumer = metadataconsumer
        self._num_of_steps = int(self._Config.GetConfigValueForSectionAndKey('RunDefinations', 'NumberOfSteps', 200))
        self._ants_producer = antsproducer
        self._Ants = []
        self._EvaulationWrapper = evaulationWrapper

    def Process(self)->ComposedEvaluationResponse:
        with PerformanceCounter("Process",self._performance_writter_wrapper):

            self._ants_meta_data_consumer.ProcessPreRun(self._num_of_steps, self._Maze, self._GetPreTestAdditionalData())
            counter=0

            while counter<self._num_of_steps:
                with PerformanceCounter("Colony_Step", self._performance_writter_wrapper):
                    counter+=1
                    self._ants_meta_data_consumer.ProcessPreSysStep(counter,
                                                                 self._world_image_provider.GetWorldImage(),
                                                                 self._GetPrePreStepAdditionalData())
                    ants_to_add = self._ants_producer.added_ants(counter - 1,
                                                                 self._world_image_provider.GetWorldImage())
                    self._Ants = self._Ants + ants_to_add
                    for ant in self._Ants:
                        with PerformanceCounter(format(f"Ant_{ant.ID} step"), self._performance_writter_wrapper):
                            antworldimage=self._world_image_provider.GetAntWorldImage(ant)
                            step, antAdditionalData = ant.GetStep(antworldimage)
                            self._world_image_provider.ProcessStep(ant, step)
                            self._ants_meta_data_consumer.ProcessAntStep(counter, ant, antworldimage, step,
                                                                         antAdditionalData)
                            response=self._EvaulationWrapper.EvalAntStep(ant,antworldimage,step,antAdditionalData)
                            if not self._MayContinueAfterEvalAntStep(response):
                                return response
                    self._world_image_provider.UpdatePositionsAccordingToMoves()
                    self._ants_meta_data_consumer.ProcessPostSysStep(counter, self._world_image_provider.GetWorldImage(), self._GetPostStepAdditionalData())

            self._ants_meta_data_consumer.ProcessPreStopRun(self._num_of_steps, self._world_image_provider.GetWorldImage(),
                                                            self._GetPostTestAdditionalData())
    @abstractmethod
    def _GetPreTestAdditionalData(self) -> Dict:
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
