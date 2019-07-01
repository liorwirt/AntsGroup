import numpy as np
import random

from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import AntType, NodeStateEnum

from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import GetNeighbours
from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import Dijkstra


# stability factor should be <= 1
class AntPathPlanner:
	def __init__(self, safetyRadius: int, cellTypeWeights, stabilityFactor: float, currentPosition: Position):
		self.__SafetyRadius = safetyRadius
		self.__CellWeights = cellTypeWeights
		self.__CurrentDestinationPosition = currentPosition
		self.__CurrentDestinationPrice = 0
		self.__StabilityFactor = stabilityFactor

	def PlanPath(self, worldImage: BaseSingleAntWorldImage, startingPosition: Position):
		WeightedMatrix = self.__ConvertWorldImageToWeightedMatrix(startingPosition, worldImage)
		PriceMatrix = Dijkstra(WeightedMatrix, startingPosition)
		self.__CurrentDestinationPrice = PriceMatrix[
			self.__CurrentDestinationPosition.X, self.__CurrentDestinationPosition.Y]

		self.__CurrentDestinationPosition, self.__CurrentDestinationPrice = self.__SelectDestination(PriceMatrix,
																									 WeightedMatrix,
																									 startingPosition)
		# calculate a path to the destination
		Path = self.__CalculatePathToDestination(startingPosition, self.__CurrentDestinationPosition, PriceMatrix)
		return Path[0], {}

	def __SelectDestination(self, PriceMatrix, WeightedMatrix, startingPosition):
		CandidateDestinationsPositions, CandidateDestionationsPrices = self.__CreateCandidateDestinationsList(
			PriceMatrix, WeightedMatrix)

		# pick a destination based inversely on the price of reaching that destination
		SumPrices = sum(CandidateDestionationsPrices)
		CandidateDestionationsProbabilities = [Price / SumPrices for Price in
											   CandidateDestionationsPrices]
		SelectedCandidateDestination = np.random.choice(CandidateDestinationsPositions,
														p=CandidateDestionationsProbabilities)
		SelectedCandidatePrice = CandidateDestionationsPrices[
			CandidateDestinationsPositions.index(SelectedCandidateDestination)]

		# decide if we want to switch destinations
		# we might have arrived at the current one, or the new one is too attractive
		# lower price means candidate is more attractive
		if self.__CurrentDestinationPosition == startingPosition or \
				SelectedCandidatePrice < self.__CurrentDestinationPrice * self.__StabilityFactor:
			return [SelectedCandidateDestination, SelectedCandidatePrice]
		else:
			return [self.__CurrentDestinationPosition, self.__CurrentDestinationPrice]

	def __CreateCandidateDestinationsList(self, PriceMatrix, WeightedMatrix):
		CandidateDestinationsPositions = []
		CandidateDestionationsPrices = []
		[height, width] = WeightedMatrix.shape

		# TODO use np.where, np.array.toList instead of iteration
		for pos_x in range(0, width):
			for pos_y in range(0, height):
				if (PriceMatrix[pos_x][pos_y] != np.inf) and (
						WeightedMatrix[pos_x][pos_y] == self.__CellWeights[NodeStateEnum.UnExplored]):
					CandidateDestinationsPositions.append(Position(pos_x, pos_y))
					CandidateDestionationsPrices.append(PriceMatrix[pos_x][pos_y])
		return CandidateDestinationsPositions, CandidateDestionationsPrices

	'''
	safety radius as Manhattan distance, because it's the number of steps an ant will take
	'''

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

	def __CalculatePathToDestination(self, startingPosition: Position, DestinationPosition: Position, PriceMatrix):
		Path = []
		currentPosition = DestinationPosition
		while currentPosition != startingPosition:
			Path.append(currentPosition)
			currentPosition = self.__FindCheapestNeighbour(PriceMatrix, currentPosition)
		Path.reverse()

		return Path

	def __FindCheapestNeighbour(self, weightedMatrix, position: Position):
		[height, width] = weightedMatrix.shape
		weight = np.inf
		cheapestNeighbour = position
		neighbourList = GetNeighbours(position, width, height)

		# shuffle so the neighbour is chosen randomly from routes with equal cost
		random.shuffle(neighbourList)
		for neighbour in neighbourList:
			if weightedMatrix[neighbour.X][neighbour.Y] < weight:
				weight = weightedMatrix[neighbour.X][neighbour.Y]
				cheapestNeighbour = neighbour

		return cheapestNeighbour

	def __MarkNodeNeighboursWithinRadius(self, position: Position, radius: int, inputMatrix: np.ndarray,
										 nodeValue: int):
		if -1 == radius:
			return inputMatrix
		if 0 == radius:
			inputMatrix[position.X, position.Y] = nodeValue
			return inputMatrix

		[height, width] = inputMatrix.shape
		for neighbour in GetNeighbours(position, width, height):
			inputMatrix = self.__MarkNodeNeighboursWithinRadius(neighbour, radius - 1, inputMatrix, nodeValue)

		return inputMatrix
