from abc import ABC,abstractmethod
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage

from AntenaProject.AntZTest.AntsRunEvaluation.BaseEvaluationResponse import BaseEvaluationResponse
class BaseRunEvaluation(ABC):
    def __init__(self,config):
        self._config=config

    @abstractmethod
    def EvalAntStep(self,ant:BasicAnt,antworldimage:BaseSingleAntWorldImage,move:AntStep, aditionaldata)->BaseEvaluationResponse:
        pass

    @abstractmethod
    def EvalWorldState(self,worldimage:BaseTotalWorldImage, aditionaldata)->BaseEvaluationResponse:
        pass