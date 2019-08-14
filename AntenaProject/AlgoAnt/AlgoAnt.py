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
		self.role = AntType.Scout
		# TODO get cell weights from configuration.
		self.__cellWeights = {NodeStateEnum.Clear: CellWeights.ExploredCell,
							  NodeStateEnum.Obs: np.inf,
							  NodeStateEnum.UnExplored: CellWeights.UnexploredCell,
							  NodeStateEnum.Ant: np.inf}
		# TODO get safety radius and stabilityFactor from configuration.
		self.__safetyRadius = -1  # -1 means ignore collisions
		self.__stabilityFactor = 0.9
		self.__pathPlanner = AntPathPlanner(self.__safetyRadius, self.__cellWeights, self.__stabilityFactor,
											self.CurrentPosition)

	def __validTransmissionNeighborExists(self, ants, visibleMaze):
		# TODO neighborRadius should be moved to Params.
		# TODO should turn into a transmission if NEXT step takes you out of bounds
		# TODO sometimes ants stop inexplicably, needs to be debugged.
		# neighborRadius = 10.0
		# for ant in ants.values():
		# 	if ant.role == AntType.Transmission and \
		# 			isInRange(visibleMaze, neighborRadius, ant.CurrentPosition, self.CurrentPosition):
		# 		return True
        #
		# return False
		return True


	def _internalGetStepTransmission(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
		return self._CurrentPosition, {}


	def _internalGetStepScout(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
		fellowAnts = antworldstate.Ants()
		visibleMaze = antworldstate.VisibleNodes

		if not self.__validTransmissionNeighborExists(fellowAnts, visibleMaze):
			self.role = AntType.Transmission
			return self._CurrentPosition, {}

		return self.__pathPlanner.PlanPath(antworldstate, self._CurrentPosition)


	def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
		if self.role == AntType.Transmission:
			return self._internalGetStepTransmission(antworldstate)

		elif self.role == AntType.Scout:
			return self._internalGetStepScout(antworldstate)

		raise RuntimeError(f'Logic error - unexpected self.role {self.role}')
