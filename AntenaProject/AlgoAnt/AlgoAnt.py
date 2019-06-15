from typing import Tuple, Dict
import numpy as np
from AntenaProject.Common.AntsBasicStructures.Enums import AntType, NodeStateEnum, CellWeights
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt, Position, BaseSingleAntWorldImage
from AntenaProject.AlgoAnt.AntPathPlanning.AntPathPlanner import AntPathPlanner


class AlgoAnt(BasicAnt):

    def __init__(self, id: int, config, position: Position):
        super().__init__(id, config)
        super().UpdatePosition(position)
        self.role = AntType.Scout
        self.__cellWeights = {NodeStateEnum.Clear: CellWeights.ExploredCell,
                              NodeStateEnum.Obs: np.inf,
                              NodeStateEnum.UnExplored: CellWeights.UnexploredCell,
                              NodeStateEnum.Ant: np.inf}
        # TODO get safety radius from configuration.
        self.__safetyRadius = 2

    def __validTransmissionNeighborExists(self, ants, visibleMaze):
        return True

    def _internalGetStepTransmission(self,  antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
        return self._CurrentPosition, {}

    def _internalGetStepScout(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
        fellowAnts = antworldstate.Ants()
        visibleMaze = antworldstate.VisibleNodes

        if not self.__validTransmissionNeighborExists(fellowAnts, visibleMaze):
            self.role = AntType.Transmission
            return self._CurrentPosition, {}

        pathPlanner = AntPathPlanner(antworldstate, self.__safetyRadius, self.__cellWeights, self._CurrentPosition)
        return pathPlanner.PlanPath()

    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:

        if self.role == AntType.Transmission:
            return self._internalGetStepTransmission(antworldstate)

        elif self.role == AntType.Scout:
            return self._internalGetStepScout(antworldstate)

        raise RuntimeError(f'Logic error - unexpected self.role {self.role}')



