from AntenaProject.AntZTest.AntsRunEvaluation.BaseRunEvaluation import BaseRunEvaluation
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.AntZTest.AntsRunEvaluation.Enums import EvaluationResponseEnum

from AntenaProject.AntZTest.AntsRunEvaluation.BaseEvaluationResponse import BaseEvaluationResponse


class SimpleAntEvaluator(BaseRunEvaluation):

    def __init__(self,config):
        BaseRunEvaluation.__init__(self,config)
        self.__AllowedTurnsWithOutMovement=int(self._config.GetConfigValueForSectionAndKey('RunDefinations', 'AllowedTurnsWithOutMovement'))
        self.__LastMovedTimeAndLocation={}
    def EvalAntStep(self, ant: BasicAnt, antworldimage: BaseSingleAntWorldImage, move: AntStep,
                    aditionaldata) -> BaseEvaluationResponse:
        if(ant.ID not in self.__LastMovedTimeAndLocation):
            self.__LastMovedTimeAndLocation[ant.ID]=[0,move.Position]
            return BaseEvaluationResponse(EvaluationResponseEnum.OK)
        else:
            record=self.__LastMovedTimeAndLocation[ant.ID]
            if(move.Position==record[1]):
                if (record[0]+1)>self.__AllowedTurnsWithOutMovement:
                    return BaseEvaluationResponse(EvaluationResponseEnum.Error,format(f"MotionLess allowed turns is {self.__AllowedTurnsWithOutMovement} and ant {ant.ID} was motionless for more"))
                else:
                    self.__LastMovedTimeAndLocation[ant.ID] = [record[0]+1, move.Position]
                    return BaseEvaluationResponse(EvaluationResponseEnum.Warning, format(
                        f"MotionLess allowed turns is {self.__AllowedTurnsWithOutMovement} and ant {ant.ID} was motionless for {record[0]}"))

            else:
                self.__LastMovedTimeAndLocation[ant.ID] = [0, move.Position]
                return BaseEvaluationResponse(EvaluationResponseEnum.OK)
    def EvalWorldState(self, worldimage: BaseTotalWorldImage, aditionaldata) -> BaseEvaluationResponse:
        return BaseEvaluationResponse(EvaluationResponseEnum.OK)