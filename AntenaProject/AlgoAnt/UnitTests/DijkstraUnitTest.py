from unittest import TestCase
import numpy as np

from AntenaProject.AlgoAnt.AntPathPlanning.Dijkstra import Dijkstra
from AntenaProject.Common.AntsBasicStructures.Position import Position


class TestDijkstra(TestCase):

	def test_UniformGrid(self):
		InputGrid = np.full((5, 5), 1)
		ResultGrid = Dijkstra(InputGrid, Position(0, 0))

		for i in range(5):
			for j in range(5):
				self.assertTrue(ResultGrid[i, j] == i + j)

	# A Blocked node will have a weight of infinity
	def test_BlockedGrid(self):
		InputGrid = np.full((5, 5), 1.0)
		InputGrid[2:4, 2:4] = np.inf
		ResultGrid = Dijkstra(InputGrid, Position(0, 0))

		self.assertTrue(np.all(np.equal(ResultGrid[2:4, 2:4], np.full((2, 2), np.inf))), str(ResultGrid[2:4, 2:4]))

	# An unreachable node will have a weight of infinity
	def test_UnreachableNodeGrid(self):
		InputGrid = np.full((5, 5), 1.0)
		InputGrid[2:4, 2:4] = np.inf
		InputGrid[4, 4] = 1.0
		ResultGrid = Dijkstra(InputGrid, Position(0, 0))

		self.assertTrue(np.all(np.equal(ResultGrid[2:4, 2:4], np.full((2, 2), np.inf))), str(ResultGrid[2:4, 2:4]))

	def test_NonUniformGrid(self):
		InputGrid = np.zeros((5, 5))
		for i in range(5):
			for j in range(5):
				InputGrid[i, j] = float(i + j)

		ResultGrid = Dijkstra(InputGrid, Position(0, 0))
		for j in range(5):
			for i in range(5):
				self.assertTrue(ResultGrid[i, j] == ((i + j) * (i + j + 1.0)) / 2.0)

	# large blocked area forces c shaped path
	def test_LongPathGrid(self):
		InputGrid = np.full((5, 5), 1.0)
		InputGrid[1:4, 0:4] = np.inf
		ResultGrid = Dijkstra(InputGrid, Position(0, 0))
		print(InputGrid)
		self.assertEqual(ResultGrid[4, 0], 12.0, str(ResultGrid))
