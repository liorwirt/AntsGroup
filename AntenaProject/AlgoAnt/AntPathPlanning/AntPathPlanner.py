import numpy as np

from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import AntType, NodeStateEnum

from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import GetNeighbours
from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import Dijkstra


class AntPathPlanner:
	def __init__(self, safetyRadius: int, cellTypeWeights):
		self.__SafetyRadius = safetyRadius
		self.__CellWeights = cellTypeWeights

	# self.__CurrentDestination = CurrentDestination
	# receive list of weights

	def PlanPath(self, worldImage: BaseSingleAntWorldImage, startingPosition: Position):
		WeightedMatrix = self.__ConvertWorldImageToWeightedMatrix(startingPosition, worldImage)

	# run dijkstra on matrix
	# choose a destination
	# decide if we want to switch destinations (we might have arrived at the current one)
	# calculate a path to the destination
	# return the destination

	'''
	safety radius as Manhattan distance, because it's the number of steps an ant will take
	'''

	# def __ConvertWorldImageToWeightedMatrix(self, startingPosition: Position, worldImage: BaseSingleAntWorldImage):
	def __ConvertWorldImageToWeightedMatrix(self, startingPosition: Position, worldImage: BaseSingleAntWorldImage):
		resultMatrix = np.zeros(worldImage.WorldImage.shape)

		[height, width] = worldImage.WorldImage.shape

		for pos_x in range(0, width):
			for pos_y in range(0, height):
				resultMatrix[pos_x][pos_y] = self.__CellWeights[worldImage.WorldImage[pos_x][pos_y]]

		resultMatrix[startingPosition.X, startingPosition.Y] = self.__CellWeights[NodeStateEnum.Clear]

		# mark a safety radius around scout ants
		if len(worldImage.Ants()) > 0:
			for ant in worldImage.Ants().values():
				if ant.CurrentPosition == startingPosition:
					continue

				if ant.Type() == AntType.Scout:
					resultMatrix = self.__MarkNodeNeighboursWithinRadius(ant.CurrentPosition,
																		 self.__SafetyRadius,
																		 resultMatrix,
																		 self.__CellWeights[NodeStateEnum.Ant])

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
