from AntenaProject.AntZTest.AntsRunEvaluation.BaseEvaluationResponse import BaseEvaluationResponse
from AntenaProject.AntZTest.AntsRunEvaluation.ExceptionEvaluationResponse import ExceptionEvaluationResponse
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
class ComposedEvaluationResponse(object):
    def __init__(self):
        self._State=EvaluationResponseEnum.OK
        self._Reposnses=[]


    def AddResponse(self,response):
        self._Reposnses.append(response)
        self._State=max(self._State,response.State)
    @property
    def State(self):
        return self._State
    @property
    def Responses(self):
        return self._Reposnses

    @staticmethod
    def GetOkResult():
        composite=ComposedEvaluationResponse()
        composite.AddResponse(BaseEvaluationResponse(EvaluationResponseEnum.OK))
        return composite

    @staticmethod
    def GetExceptionResult(excetionStr:str):
        composite = ComposedEvaluationResponse(ExceptionEvaluationResponse(excetionStr))
        return composite