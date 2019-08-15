

from abc import ABC, abstractmethod
from typing import List
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
from AntenaProject.AntZTest.AntsMetaDataConsumer.MetaDataToNodeStateInterperter import MetaDataToNodeStateInterperter

class DummyMetaDataToNodeStateInterperter(MetaDataToNodeStateInterperter):

    def Interpert(self, antworldstate) -> List[NodeState]:
        return  antworldstate