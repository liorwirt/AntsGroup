from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.SimpleExample.SimpleSingleAntWorldImage import SimpleSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.SimpleExample.SimpleTotalWorldImage import SimpleTotalWorldImage
import numpy as np


class UnifiedWorldImageProvider(BasicWorldImageProvider):

    def __init__(self, config, maze):
        BasicWorldImageProvider.__init__(self, config, maze)
        self.__AntsPlannedStepDict = {}
        self.__AntsWorldImage = {}
        self.__ExploredCells = np.zeros(maze.GetDims())
        self.__CombinedMap = np.zeros(maze.GetDims())
        self.__Ants = {}
        self.__VisibilityRange = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "VisibilityRange", 1))
        self.__AllowedMovement = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "AllowedMovement", 1))

    def ProcessStep(self, ant: BasicAnt, step: AntStep):
        if self._Maze.MayMove(ant.CurrentPosition, step.Position, self.__AllowedMovement):
            self.__AntsPlannedStepDict[ant.ID] = (ant, step)

    def GetAntWorldImage(self, ant: BasicAnt) -> BaseSingleAntWorldImage:
        antWorldImage = self.__GetPerAntGlobalWorldImage()
        self.__AntsWorldImage[ant.ID] = antWorldImage
        return antWorldImage

    def __GetPerAntGlobalWorldImage(self):
        return SimpleSingleAntWorldImage(self.__CombinedMap)

    def GetWorldImage(self) -> BaseTotalWorldImage:
        return SimpleTotalWorldImage(self.__AntsWorldImage, self.__CombinedMap)

    def UpdatePositionsAccordingToMoves(self):
        for value in self.__AntsPlannedStepDict.values():
            step = value[1]
            ant = value[0]
            ant.UpdatePosition(step.Position)
            self.__Ants[ant.ID] = ant
            self.__UpdateExploredStepsPerAnt(step.Position)

        self.__GenrateCombinedMap()
        self.__AntsPlannedStepDict.clear()

    def __GetBB(self, radius: int, position: Position):
        leftMost = max(0, position.X - radius)
        rightMost = min(self._Maze.GetDims()[1] - 1, position.X + radius)

        topMost = max(0, position.Y - radius)
        bottomMost = min(self._Maze.GetDims()[0] - 1, position.Y + radius)
        return leftMost, rightMost, topMost, bottomMost

    def __UpdateExploredStepsPerAnt(self, position: Position):
        self.__ExploredCells[position.Y][position.X] = 1
        leftMost, rightMost, topMost, bottomMost = self.__GetBB(position=position, radius=self.__VisibilityRange)

        for pos_x in range(leftMost, rightMost + 1):
            for pos_y in range(topMost, bottomMost + 1):
                self.__ExploredCells[pos_y][pos_x] = 1

    def __GenrateCombinedMap(self):

        [height, width] = self.__ExploredCells.shape
        for pos_x in range(0, width):
            for pos_y in range(0, height):
                if self.__ExploredCells[pos_y][pos_x] == 0:
                    self.__CombinedMap[pos_y][pos_x] = NodeStateEnum.UnExplored
                else:
                    if self._Maze.IsObs(Position(x=pos_x, y=pos_y)):
                        self.__CombinedMap[pos_y][pos_x] = NodeStateEnum.Obs
                    else:
                        self.__CombinedMap[pos_y][pos_x] = NodeStateEnum.Clear
        for ant in self.__Ants.values():
            self.__CombinedMap[ant.CurrentPosition.Y][ant.CurrentPosition.X] = ant.Type()
