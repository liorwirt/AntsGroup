from abc import ABC,abstractmethod
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from typing import Tuple
class BasicAnt(ABC):
    def __init__(self,id:int,config):
        self._Config=config
        self._ID=id
        self._CurrentPosition=Position.GetEmptyPoistion()


    @property
    def ID(self):
        return self._ID

    @property
    def CurrentPosition(self):
        return self._CurrentPosition

    @abstractmethod
    def _internalGetStep(self,antworldstate:BaseSingleAntWorldImage)->Position:
        pass

    def UpdatePosition(self,position:Position):
        self._CurrentPosition=position

    def GetStep(self,antworldstate:BaseSingleAntWorldImage)->AntStep:
        return AntStep(self._ID,self._internalGetStep(antworldstate))
