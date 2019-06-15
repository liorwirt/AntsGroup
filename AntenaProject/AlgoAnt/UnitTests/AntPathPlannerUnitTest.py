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


class TestPathPlanner(TestCase):

	def test_EmptyGrid(self):
		Maze = MazeFacade(DIYMazeParser(8))
		Provider = UnifiedWorldImageProvider(maze=Maze, config=DictionaryConfigProvider())

		weights = {NodeStateEnum.Clear: 2,
				   NodeStateEnum.Obs: np.inf,
				   NodeStateEnum.UnExplored: 1,
				   NodeStateEnum.Ant: np.inf}

		Planner = AntPathPlanner(Provider.GetWorldImage(), safetyRadius=2, cellTypeWeights=weights,
								 startingPosition=Position(0, 0))

		result = Planner.WeightedMatrix

		print(result)

		Width, Height = result.shape

		for i in range(0, Width):
			for j in range(0, Height):
				if i == 0 and j == 0:
					self.assertEqual(result[i][j], weights[NodeStateEnum.Clear])
				else:
					self.assertEqual(result[i][j], weights[NodeStateEnum.UnExplored])

	def test_SingleScout(self):
		Maze = MazeFacade(DIYMazeParser(8))
		WorldImageProvder = UnifiedWorldImageProvider(maze=Maze, config=DictionaryConfigProvider())

		weights = {NodeStateEnum.Clear: 2,
				   NodeStateEnum.Obs: np.inf,
				   NodeStateEnum.UnExplored: 1,
				   NodeStateEnum.Ant: np.inf}

		ant = AlgoAnt(id=1, config=DictionaryConfigProvider(), position=Position(3, 3))

		WorldImageProvder.ProcessStep(ant, AntStep(ant.ID, ant.CurrentPosition))

		Planner = AntPathPlanner(WorldImageProvder.GetWorldImage(), safetyRadius=2, cellTypeWeights=weights,
								 startingPosition=Position(0, 0))

		result = Planner.WeightedMatrix

		print(result)
