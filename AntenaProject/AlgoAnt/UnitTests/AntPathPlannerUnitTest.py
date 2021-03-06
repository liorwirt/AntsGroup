from unittest import TestCase
import numpy as np

from AntenaProject.AlgoAnt.WorldImage.UnifiedWorldImageProvider import UnifiedWorldImageProvider
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Maze.Parsers.DIYMazeParser import DIYMazeParser
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.AlgoAnt.AntPathPlanning.AntPathPlanner import AntPathPlanner
from AntenaProject.Common.Config.DictionaryConfigProvider import DictionaryConfigProvider
from AntenaProject.AlgoAnt.AlgoAnt import AlgoAnt
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.SimpleExample.SimpleSingleAntWorldImage import SimpleSingleAntWorldImage
from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import Dijkstra


class TestPathPlanner(TestCase):

	def test__ConvertWorldImageToWeightedMatrix_EmptyGrid(self):
		Maze = MazeFacade(DIYMazeParser(8))
		Provider = UnifiedWorldImageProvider(maze=Maze, config=DictionaryConfigProvider())

		weights = {NodeStateEnum.Clear: 2,
				   NodeStateEnum.Obs: np.inf,
				   NodeStateEnum.UnExplored: 1,
				   NodeStateEnum.Ant: np.inf}

		Planner = AntPathPlanner(safetyRadius=2, cellTypeWeights=weights, stabilityFactor=1)
		StartPosition = Position(0, 0)
		mazeMatrix = Maze.GetMatrix()
		manuallyAdjustedMaze = np.where(mazeMatrix == 1, NodeStateEnum.UnExplored, NodeStateEnum.Clear)
		manuallyAdjustedMaze[0, 0] = NodeStateEnum.Clear
		singleAntWorldImage = SimpleSingleAntWorldImage(manuallyAdjustedMaze, {})
		result = Planner._AntPathPlanner__ConvertWorldImageToWeightedMatrix(StartPosition, singleAntWorldImage)

		Width, Height = result.shape

		for i in range(0, Width):
			for j in range(0, Height):
				if i == 0 and j == 0:
					self.assertEqual(result[i][j], weights[NodeStateEnum.Clear])
				else:
					self.assertEqual(result[i][j], weights[NodeStateEnum.UnExplored])

	'''
	in a uniform grid, the weights on the route should increase by 1 each step
	'''

	def test__CalculatePathToDestination_UniformGrid(self):
		Maze = MazeFacade(DIYMazeParser(8))
		Provider = UnifiedWorldImageProvider(maze=Maze, config=DictionaryConfigProvider())

		weights = {NodeStateEnum.Clear: 2,
				   NodeStateEnum.Obs: np.inf,
				   NodeStateEnum.UnExplored: 1,
				   NodeStateEnum.Ant: np.inf}

		Planner = AntPathPlanner(safetyRadius=2, cellTypeWeights=weights, stabilityFactor=1)
		StartPosition = Position(0, 0)
		mazeMatrix = Maze.GetMatrix()
		manuallyAdjustedMaze = np.where(mazeMatrix == 1, NodeStateEnum.UnExplored, NodeStateEnum.Clear)
		manuallyAdjustedMaze[0, 0] = NodeStateEnum.Clear
		singleAntWorldImage = SimpleSingleAntWorldImage(manuallyAdjustedMaze, {})
		weightedMatrix = Planner._AntPathPlanner__ConvertWorldImageToWeightedMatrix(StartPosition, singleAntWorldImage)
		pathMatrix = Dijkstra(weightedMatrix, StartPosition)

		resultRoute = Planner._AntPathPlanner__CalculatePathToDestination(StartPosition, Position(4, 4), pathMatrix)

		weightSum = 0

		for position in resultRoute:
			weightSum += weightedMatrix[position.X][position.Y]
			self.assertEqual(pathMatrix[position.X][position.Y], weightSum)

		def printRoute(route):
			for position in route:
				print(f'[{position.X}, {position.Y}] ')

	# printRoute(resultRoute)


'''
should return an unexplored matrix except for a scout ant at position (3,3) with radius 0 safety radius
'''


def test_SingleScout(self):
	Maze = MazeFacade(DIYMazeParser(8))
	Provider = UnifiedWorldImageProvider(maze=Maze, config=DictionaryConfigProvider())

	weights = {NodeStateEnum.Clear: 2,
			   NodeStateEnum.Obs: np.inf,
			   NodeStateEnum.UnExplored: 1,
			   NodeStateEnum.Ant: np.inf}

	ant = AlgoAnt(id=1, config=DictionaryConfigProvider(), position=Position(3, 3))

	Provider.ProcessStep(ant, AntStep(ant.ID, ant.CurrentPosition))
	Provider.UpdatePositionsAccordingToMoves()
	Planner = AntPathPlanner(safetyRadius=0, cellTypeWeights=weights)

	result = Planner._AntPathPlanner__ConvertWorldImageToWeightedMatrix(Position(0, 0),
																		Provider.GetAntWorldImage(ant))

	print(result)
