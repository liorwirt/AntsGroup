from AntenaProject.AntZTest.AntsController.BaseAntsController import BaseAntsController
from typing import Dict
from AntenaProject.AntZTest.AntsRunEvaluation.ComposedEvaluationResponse import ComposedEvaluationResponse
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
import logging
class SimpleAntsContrller(BaseAntsController):

    def _GetPreTestAdditionalData(self) -> Dict:
        return {}


    def _GetPrePreStepAdditionalData(self) -> Dict:
        return {}


    def _GetPostStepAdditionalData(self) -> Dict:
        return {}


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