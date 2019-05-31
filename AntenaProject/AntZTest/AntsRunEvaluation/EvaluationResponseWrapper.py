import traceback
from  AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.AntZTest.AntsRunEvaluation.BaseEvaluationResponse import BaseEvaluationResponse
from AntenaProject.AntZTest.AntsRunEvaluation.ComposedEvaluationResponse import ComposedEvaluationResponse
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.AntZTest.AntsRunEvaluation.BaseRunEvaluation import BaseRunEvaluation
from AntenaProject.AntZTest.AntsRunEvaluation.ExceptionEvaluationResponse import ExceptionEvaluationResponse
class EvaluationResponseWrapper(BaseRunEvaluation):
    def __init__(self,config):
        self.__Evaluators=[]
    def AddEvaluator(self,consumer:BaseRunEvaluation):
        self.__Evaluators.append(consumer)

    def EvalAntStep(self,ant:BasicAnt,antworldimage:BaseSingleAntWorldImage,move:AntStep, aditionaldata)->ComposedEvaluationResponse:
        response = ComposedEvaluationResponse()

        try:
            for evaluator in self.__Evaluators:
                response.AddResponse(evaluator.EvalAntStep(ant,antworldimage, move,aditionaldata))
        except Exception as e:
            traceback.print_exc()
            response.AddResponse(ExceptionEvaluationResponse(traceback.format_exc()))
            return response

        return response

    def EvalWorldState(self,worldimage:BaseTotalWorldImage, aditionaldata)->ComposedEvaluationResponse:
        response = ComposedEvaluationResponse()

        try:
            for evaluator in self.__Evaluators:
                response.AddResponse(evaluator.EvalWorldState(worldimage, aditionaldata))
        except Exception as e:
            traceback.print_exc()
            response.AddResponse(ExceptionEvaluationResponse(traceback.format_exc()))
            return response
        return response

