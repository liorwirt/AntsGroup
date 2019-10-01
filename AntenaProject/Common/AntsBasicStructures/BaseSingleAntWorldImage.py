import numpy as np
from abc import ABC,abstractproperty,abstractmethod
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
from AntenaProject.Common.AntsBasicStructures.Position import Position
from typing import List



class BaseSingleAntWorldImage(ABC):
    def __init__(self,id,pos:Position):
        self._id=id
        self._position=pos
    @property
    @abstractmethod
    def VisibleNodes(self) -> List[NodeState]:
        pass

    @property
    @abstractmethod
    def WorldImage(self):
        pass

    @abstractmethod
    def Ants(self):
        """
        :return: Fellow Ants in the maze, along with their last update time (per ant).
        """
        pass
