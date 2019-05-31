from abc import ABC,abstractmethod
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum
class BaseEvaluationResponse(ABC):
    def __init__(self,state=EvaluationResponseEnum.OK,messege='All is Fine'):
        self._State=state
        self._Messege=messege
    @property
    def State(self):
        return self._State

    @property
    def Messege(self):
        return self._Messege
