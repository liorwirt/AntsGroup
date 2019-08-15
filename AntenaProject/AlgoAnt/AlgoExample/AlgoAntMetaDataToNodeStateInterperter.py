from typing import List
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum


from AntenaProject.AntZTest.AntsMetaDataConsumer.MetaDataToNodeStateInterperter import MetaDataToNodeStateInterperter
import numpy as np
class AlgoAntMetaDataToNodeStateInterperter(MetaDataToNodeStateInterperter):

    def Interpert(self, antworldstate) -> List[NodeState]:
        nodes=[]
        size_of_world_image=np.shape(antworldstate)
        for x in range(size_of_world_image[0]):
            for y in range(size_of_world_image[1]):
                state=(NodeStateEnum)(antworldstate[y][x])
                if(state!=NodeStateEnum.UnExplored):
                    nodes.append(NodeState(state,Position(x,y)))

        return  nodes