from abc import ABC,abstractmethod
from multiprocessing import Process,Event
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.AntZTest.AntsRunEvaluation.ComposedEvaluationResponse import ComposedEvaluationResponse
class BaseMultiRunAgent(ABC,Process):
    def __init__(self,id,config:BaseConfigProvider,maze:MazeFacade,return_dict):
        Process.__init__(self)
        self._config=config
        self._returnDict=return_dict
        self._Maze=maze
        self._id=id

    def run(self):
        self._InternalStart()
        self._InternalProcess()
        self._returnDict[self._id]=self._ComposeResult()
        self._InternalStop()

    def terminate(self):
        self._InternalTermination()

    @abstractmethod
    def _ComposeResult(self)->ComposedEvaluationResponse:
        pass
    @abstractmethod
    def _InternalStart(self):
        pass

    @abstractmethod
    def _InternalProcess(self):
        pass

    @abstractmethod
    def _InternalStop(self):
        pass

    @abstractmethod
    def _InternalTermination(self):
        pass