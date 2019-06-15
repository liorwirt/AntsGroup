import numpy as np

from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import AntType, NodeStateEnum

from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import GetNeighbours
from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import Dijkstra


class AntPathPlanner:
	def __init__(self, worldImage: BaseTotalWorldImage, safetyRadius: int, cellTypeWeights, startingPosition: Position):
		self.startingPosition = startingPosition
		self.WeightedMatrix = self.__ConvertWorldImageToWeightedMatrix(worldImage, safetyRadius, cellTypeWeights)

	# self.__CurrentDestination = CurrentDestination
	# receive list of weights

	def PlanPath(self):
		pass

	# convert world image into weighted matrix
	# run dijkstra on matrix
	# choose a destination
	# decide if we want to switch destinations (we might have arrived at the current one)
	# calculate a path to the destination
	# return the destination

	'''
	safety radius as Manhattan distance, because it's the number of steps an ant will take
	'''

	def __ConvertWorldImageToWeightedMatrix(self, worldImage: BaseTotalWorldImage, safetyRadius: int, cellTypeWeights):
		resultMatrix = np.zeros(worldImage.WorldMatrix.shape)

		[height, width] = worldImage.WorldMatrix.shape

		for pos_x in range(0, width):
			for pos_y in range(0, height):
				resultMatrix[pos_x][pos_y] = cellTypeWeights[worldImage.WorldMatrix[pos_x][pos_y]]

		resultMatrix[self.startingPosition.X, self.startingPosition.Y] = cellTypeWeights[NodeStateEnum.Clear]

		# mark a safety radius around scout ants
		for ant in worldImage.Ants().values():
			if ant.CurrentPosition == self.startingPosition:
				continue

			if ant.Type() == AntType.Scout:
				self.__MarkNodeNeighboursWithinRadius(ant.CurrentPosition,
													  safetyRadius,
													  resultMatrix,
													  cellTypeWeights[NodeStateEnum.Ant])

		return resultMatrix

	def __ChooseNextDestination(self, NewDestination: Position):
		pass

	def __CalculatePathToDestination(self):
		pass

	def __MarkNodeNeighboursWithinRadius(self, position: Position, radius: int, inputMatrix: np.ndarray,
										 nodeValue: int):
		if 0 == radius:
			inputMatrix[position.X, position.Y] = nodeValue
			return inputMatrix

		[height, width] = inputMatrix.shape
		for neighbour in GetNeighbours(position, width, height):
			inputMatrix = self.__MarkNodeNeighboursWithinRadius(neighbour, radius - 1, inputMatrix, nodeValue)

		return inputMatrix
