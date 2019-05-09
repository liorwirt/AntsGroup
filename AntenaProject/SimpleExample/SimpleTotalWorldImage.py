from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
from typing import List
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
import numpy as np
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
class SimpleTotalWorldImage(BaseTotalWorldImage):

    def __init__(self,antsWorldImage,combinedMap:np.matrix):
        self.__AntsWorldImage=antsWorldImage
        self.__CombinedMap=combinedMap

    def GetNodesState(self,*positions:Position)->List[NodeState]:
        results =[]
        for pos in positions:
            if pos.X<=self.__CombinedMap.shape[1] and pos.Y<=self.__CombinedMap.shape[0]:
                results.append(NodeState(NodeStateEnum(self.__CombinedMap[pos.Y][pos.X]),pos))
            else:
                results.append(None)
        return results

    def GetAntsWorldImage(self, *ants:BasicAnt) -> List[BaseSingleAntWorldImage]:
        results=[]
        for ant in ants:
            if ant.ID in self.__AntsWorldImage:
                results.append(self.__AntsWorldImage[ant.ID])
            else:
                results.append(None)
        return results
    @property
    def WorldMatrix(self):
        return self.__CombinedMap

    @property
    def Coverage(self):
       howmuschisunexplored=np.count_nonzero(self.__CombinedMap == NodeStateEnum.UnExplored)
       mazesize=self.__CombinedMap.shape[0] *self.__CombinedMap.shape[1]

       return float(((mazesize-howmuschisunexplored)*100)/mazesize)