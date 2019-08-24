from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.SimpleExample.SimpleSingleAntWorldImage import SimpleSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.SimpleExample.SimpleTotalWorldImage import SimpleTotalWorldImage
from AntenaProject.AntZTest.Commands.CommandsReciver import CommandsReciver
from AntenaProject.Common.AntsBasicStructures.AlgExternalCommand import AlgExternalCommand
from AntenaProject.Common.AntsBasicStructures.Enums import AlgCommandEnum
import numpy as np
import time


class UnifiedWorldImageProvider(BasicWorldImageProvider):

    def __init__(self, config, maze, commandreciver: CommandsReciver):
        super().__init__(config, maze, )
        self.__AntsPlannedStepDict = {}
        self.__AntsWorldImage = {}
        self.__ExploredCells = np.zeros(maze.GetDims())
        self.__CombinedMap = np.full(maze.GetDims(), NodeStateEnum.UnExplored)
        self.__Ants = {}
        self.__VisibilityRange = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "VisibilityRange", 1))
        self.__AllowedMovement = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "AllowedMovement", 1))
        self.__CommandsToWeights = {}
        self.__CommandsToWeights[AlgCommandEnum.Priority] = int(
            self._Config.GetConfigValueForSectionAndKey("CommandsWeight", "Priority", 1))
        self.__CommandsToWeights[AlgCommandEnum.Clear] = int(
            self._Config.GetConfigValueForSectionAndKey("CommandsWeight", "Clear", 1))
        self.__CommandsReceiver = commandreciver

    def ProcessStep(self, ant: BasicAnt, step: AntStep):
        if self._Maze.MayMove(ant.CurrentPosition, step.Position, self.__AllowedMovement):
            self.__AntsPlannedStepDict[ant.ID] = (ant, step)

    def GetAntWorldImage(self, ant: BasicAnt) -> BaseSingleAntWorldImage:
        antWorldImage = self.__GetPerAntGlobalWorldImage()
        self.__AntsWorldImage[ant.ID] = antWorldImage
        return antWorldImage

    def __GetPerAntGlobalWorldImage(self):
        return SimpleSingleAntWorldImage(self.__CombinedMap, self.__Ants)

    def GetWorldImage(self) -> BaseTotalWorldImage:
        return SimpleTotalWorldImage(self.__AntsWorldImage, self.__CombinedMap, self.__Ants)

    def UpdatePositionsAccordingToMoves(self):
        for value in self.__AntsPlannedStepDict.values():
            step = value[1]
            ant = value[0]
            ant.UpdatePosition(step.Position)
            self.__Ants[ant.ID] = ant
            self.__UpdateExploredStepsPerAnt(step.Position)

        self.__GenerateCombinedMap()
        self.__AntsPlannedStepDict.clear()
        commands = self.__CommandsReceiver.GetCommands()
        for command in commands:
            self.__HandleCommand(command)

    def __HandleCommand(self, command: AlgExternalCommand):
        if (command.Command in self.__CommandsToWeights):
            for ant in self.__Ants.values():
                ant.UpdateRegionWeight(command.Position, self.__CommandsToWeights[command.Command])

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

    def __GenerateCombinedMap(self):
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
