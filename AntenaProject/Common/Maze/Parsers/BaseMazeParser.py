from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple,List
from AntenaProject.Common.AntsBasicStructures.Position import Position

coordinates=List[Position]

class BaseMazeParser(ABC):

    @property
    @abstractmethod
    def GetMatrix(self)->np.ndarray:
        pass

    @property
    @abstractmethod
    def GetEnterence(self)->Position:
        pass

    @property
    @abstractmethod
    def IsObs(self,position:Position)->bool:
        pass

    @property
    @abstractmethod
    def GetExits(self)->coordinates:
        pass

    @property
    @abstractmethod
    def GetDims(self)->(int,int):
        pass

    @property
    @abstractmethod
    def GetName(self):
        pass

