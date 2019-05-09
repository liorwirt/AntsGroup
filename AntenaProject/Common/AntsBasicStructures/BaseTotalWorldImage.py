import numpy as np
from abc import ABC,abstractproperty,abstractmethod
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from typing import List

class BaseTotalWorldImage(ABC):

    @abstractmethod
    def GetNodesState(self,*positions:Position)->List[NodeState]:
        pass

    @abstractmethod
    def GetAntsWorldImage(self, *ants:BasicAnt) -> List[BaseSingleAntWorldImage]:
        pass

    @property
    @abstractmethod
    def WorldMatrix(self):
      pass

    @property
    @abstractmethod
    def Coverage(self):
        pass
