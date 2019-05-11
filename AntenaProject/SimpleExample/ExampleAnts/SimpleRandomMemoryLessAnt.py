from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
import numpy as np
import random

class SimpleRandomMemoryLessAnt(BasicAnt):
    def __init__(self,id:int,config):
        BasicAnt.__init__(self,id,config)

    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage) :

        UnExplored_nodes=[]
        Clear_nodes = []
        Ant_nodes = []
        for node in antworldstate.VisibleNodes:
            if node.NodeState==NodeStateEnum.UnExplored:
                UnExplored_nodes.append(node.Position)
            if node.NodeState==NodeStateEnum.Clear:
                Clear_nodes.append(node.Position)
            if node.NodeState==NodeStateEnum.Ant:
                Ant_nodes.append(node.Position)

        if(len(UnExplored_nodes)>0):
            return self.SelctStepFromChoices(UnExplored_nodes),{}
        if (len(Clear_nodes) > 0):
            return self.SelctStepFromChoices(Clear_nodes),{}
        if (len(Ant_nodes) > 0):
            return self.SelctStepFromChoices(Ant_nodes),{}
        return self.CurrentPosition,{}

    def SelctStepFromChoices(self,choiceslist)->Position:
        selectedNode = random.choice(choiceslist)
        return selectedNode