from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple,List
coordinate = Tuple[int,int]
coordinates=List[coordinate]

class BaseMazeParser(ABC):

    @property
    @abstractmethod
    def GetMatrix(self)->np.ndarray:
        pass

    @property
    @abstractmethod
    def GetEnterence(self)->coordinate:
        pass

    @property
    @abstractmethod
    def GetExits(self)->coordinates:
        pass
    @property
    @abstractmethod
    def GetDims(self)->coordinate:
        pass
