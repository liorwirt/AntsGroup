

from AntenaProject.AntZTest.AntsRunEvaluation.BaseEvaluationResponse import BaseEvaluationResponse
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
class ExceptionEvaluationResponse(BaseEvaluationResponse):
    def __init__(self,exceptionstr):
        BaseEvaluationResponse.__init__(self,EvaluationResponseEnum.Exception,'Encountered an exception')

        self._ExceptionStr=exceptionstr
    @property
    def ExceptionStr(self):
        return self._ExceptionStr

