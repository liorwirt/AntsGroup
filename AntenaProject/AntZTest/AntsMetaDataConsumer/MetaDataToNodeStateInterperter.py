from abc import ABC,abstractmethod
from typing import List
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
class MetaDataToNodeStateInterperter(ABC):

    @abstractmethod
    def Interpert(self,antworldstate)->List[NodeState]:
        pass