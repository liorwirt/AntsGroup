from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
import numpy as np
import random

class SimpleRandomMemoryLessAnt(BasicAnt):
    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage) -> Position:
        choiceslist=[]
        for node in antworldstate.VisibleNodes:
            if node.NodeState==NodeStateEnum.UnExplored:
                choiceslist.append(node)
            if node.NodeState == NodeStateEnum.Clear and self._CurrentPosition != node.Position:
                choiceslist.append(node)
        if(len(choiceslist)>0):
            selectedNode= random.choice(choiceslist)
            return selectedNode.Position
        return self.CurrentPosition