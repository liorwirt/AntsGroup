from abc import abstractmethod,ABC
from typing import List
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
class BasicAntProducer(ABC):
    def __init__(self,config):
        self._Config=config
        self._CurrentAnt=None

    @abstractmethod
    def CreateAnts(self):
        pass
    @abstractmethod
    def _StopIteration(self)->bool:
        pass

    @abstractmethod
    def _NextAnt(self) -> BasicAnt:
        pass

    def __iter__(self):
        return self

    def __next__(self)->BasicAnt:
        if self._StopIteration():
            raise StopIteration
        else:
            return self.__NextAnt()