from typing import Tuple, Dict
import numpy as np
from AntenaProject.Common.AntsBasicStructures.Enums import AntType, NodeStateEnum, CellWeights
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt, Position, BaseSingleAntWorldImage
from AntenaProject.AlgoAnt.AntPathPlanning.AntPathPlanner import AntPathPlanner
from AntenaProject.Common.Utils.UtilFunctions import isInRange


class AlgoAnt(BasicAnt):

    def __init__(self, id: int, config, position: Position):
        super().__init__(id, config)
        super().UpdatePosition(position)
        self.SetRole(AntType.Scout)

        # TODO get parameters  from configuration.
        self.__cellWeights = {NodeStateEnum.Clear: CellWeights.ExploredCell,
                              NodeStateEnum.Obs: np.inf,
                              NodeStateEnum.UnExplored: CellWeights.UnexploredCell,
                              NodeStateEnum.Ant: CellWeights.ExploredCell}
        self.__safetyRadius = -1  # -1 means ignore collisions
        self.__stabilityFactor = 0.9
        self.__pathPlanner = AntPathPlanner(self.__safetyRadius, self.__cellWeights, self.__stabilityFactor,
                                            self.CurrentPosition)
        self.neighborRadius = 10.0

    def __validTransmissionNeighborExists(self, ants, visibleMaze, NextPosition: Position):
        # TODO sometimes ants stop inexplicably, needs to be debugged.
        for ant in ants.values():
            if ant.GetRole() == AntType.Transmission:
                InRange = isInRange(visibleMaze, self.neighborRadius, ant.CurrentPosition, NextPosition)
                if InRange:
                    return True
        return False

    def _internalGetStepTransmission(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
        return self._CurrentPosition, {}

    def _internalGetStepScout(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
        fellowAnts = antworldstate.Ants()
        visibleMaze = antworldstate.VisibleNodes

        NextPosition, Dict = self.__pathPlanner.PlanPath(antworldstate, self._CurrentPosition)

        if not self.__validTransmissionNeighborExists(fellowAnts, visibleMaze, NextPosition):
            self.SetRole(AntType.Transmission)
            return self._internalGetStepTransmission(antworldstate)

        return NextPosition, Dict

    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
        if self.GetRole() == AntType.Transmission:
            return self._internalGetStepTransmission(antworldstate)

        elif self.GetRole() == AntType.Scout:
            return self._internalGetStepScout(antworldstate)

        raise RuntimeError(f'Logic error - unexpected self.role {self.role}')

    def UpdateRegionWeight(self, position: Position, priority_multiplier):
        self.__pathPlanner.UpdateRegionWeight(position, priority_multiplier)

    def GetRole(self):
        return self._role

    def SetRole(self, NewRole):
        self._role = NewRole
