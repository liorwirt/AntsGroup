from AntenaProject.AntZTest.AntsController.BaseAntsController import BaseAntsController
from typing import Dict
from AntenaProject.AntZTest.AntsRunEvaluation.ComposedEvaluationResponse import ComposedEvaluationResponse
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
import logging
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
from AntenaProject.MeshAnts.connectivty_calculator import connectivty_calculator

class SimpleMeshAntsContrller(BaseAntsController):
    def __init__(self, config, maze, metadataconsumer: AntsMetaDataConsumerWrapper,
                 performanceCounterWrapper: PerofromanceWriterWrapper, basicWorldImageProvider: BasicWorldImageProvider,
                 antsproducer: BasicAntProducer, evaulationWrapper: EvaluationResponseWrapper,connectivty_calculator:connectivty_calculator):
        BaseAntsController.__init__(self,config,maze,metadataconsumer,performanceCounterWrapper,basicWorldImageProvider,antsproducer,evaulationWrapper)
        self._connectivty_calculator=connectivty_calculator



    def _GetPreTestAdditionalData(self) -> Dict:
        return {}


    def _GetPrePreStepAdditionalData(self) -> Dict:
        return {}


    def _GetPostStepAdditionalData(self) -> Dict:
        ants_positions={}
        for ant in self._ants_producer:
            ants_positions[ant.ID]=ant.CurrentPosition

        connectivity_lines=self._connectivty_calculator.get_connectivity_lines(ants_positions)
        additional_data={}
        additional_data["connectivity_lines"]=connectivity_lines
        return additional_data


    def _GetPostTestAdditionalData(self) -> Dict:
        return {}

    def _MayContinueAfterEvalWorldState(self, response:ComposedEvaluationResponse) -> bool:
        if(response.State==EvaluationResponseEnum.Warning) :
            logging.warning(response.Messege)
            return True
        if (response.State == EvaluationResponseEnum.OK):
            return True
        return False


    def _MayContinueAfterEvalAntStep(self, response:ComposedEvaluationResponse) -> bool:
        if (response.State == EvaluationResponseEnum.Warning):
            logging.warning('Recoved Warninng State!')
            for inneresponse in response.Responses:
                logging.info(inneresponse.Messege)
            return True
        if (response.State == EvaluationResponseEnum.OK):
            return True
        return False