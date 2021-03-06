from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
import random


class SimpleRandomMemoryLessAnt(BasicAnt):
    def __init__(self, id: int, config):
        BasicAnt.__init__(self, id, config)
        self.__Direction_X = random.choice([1, -1])
        self.__Direction_Y = random.choice([1, -1])

    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage):

        # try to keep this direction
        targetPosition = Position(self.CurrentPosition.X + self.__Direction_X,
                                  self.CurrentPosition.Y + self.__Direction_Y)

        for node in antworldstate.VisibleNodes:
            if node.Position == targetPosition and node.NodeState != NodeStateEnum.Obs:
                return targetPosition

        self.__Direction_X = random.choice([1, -1])
        self.__Direction_Y = random.choice([1, -1])
        targetPosition = Position(self.CurrentPosition.X + self.__Direction_X,
                                  self.CurrentPosition.Y + self.__Direction_Y)

        for node in antworldstate.VisibleNodes:
            if node.Position == targetPosition and node.NodeState != NodeStateEnum.Obs:
                return targetPosition

        return self.CurrentPosition, {}
