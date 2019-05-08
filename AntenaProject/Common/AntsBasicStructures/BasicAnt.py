from abc import ABC,abstractmethod
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from typing import Tuple
class BasicAnt(ABC):
    def __init__(self,id:int,config):
        self.__Config=config
        self.__ID=id
        self.__CurrentPosition=Position.GetEmptyPoistion()


    @property
    def ID(self):
        return self.__ID
    @abstractmethod
    def _internalGetStep(self,antworldstate:BaseSingleAntWorldImage)->Position:
        pass

    def UpdatePosition(self,position:Position):
        self.__CurrentPosition=position

    def GetStep(self,antworldstate:BaseSingleAntWorldImage)->AntStep:
        return AntStep(self.__ID,self._internalGetStep(antworldstate))
