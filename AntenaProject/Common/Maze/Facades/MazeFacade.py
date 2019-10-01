import numpy as np
from AntenaProject.Common.Maze.Parsers.BaseMazeParser import BaseMazeParser
import networkx as nx
from AntenaProject.Common.AntsBasicStructures.Position import Position
from networkx.readwrite import json_graph


class MazeFacade(object):

	def __init__(self, mazeparser: BaseMazeParser):
		self.__MazeParser = mazeparser

		self.__GenrateGraph()

	def GetMatrix(self) -> np.ndarray:
		return self.__MazeParser.GetMatrix()

	def GetEnterence(self):
		return self.__MazeParser.GetEnterence()

	def GetExits(self):
		return self.__MazeParser.GetExits()

	def GetDims(self):
		return self.__MazeParser.GetDims()

	def MayMove(self, src: Position, dst: Position, maxNumberOfSteps=1):
		if (src == dst):
			return True
		try:
			path = self.__GetPath(src, dst)
			# src and dst are returened
			lengthofpath = len(path) - 2
			maymove = (lengthofpath >= 0 and lengthofpath < maxNumberOfSteps)
			return maymove
		except Exception as ex:
			return False

	def IsObs(self, position: Position) -> bool:
		return self.__MazeParser.IsObs(position)


	def is_in_bounds(self, position: Position) -> bool:
		if position.Y<0 or position.X<0:
			return False
		width, height = self.__MazeParser.GetDims()
		if position.Y>height-1 or position.X>width-1:
			return False

		return True




	@property
	def ConnectivityGraph(self):
		return self.__Graph

	@property
	def Name(self):
		return self.__MazeParser.GetName()

	def __GetPath(self, src: Position, dst: Position):

		width, height = self.__MazeParser.GetDims()
		path = nx.shortest_path(self.__Graph, self.__ToGridNode(src.X, src.Y),
								self.__ToGridNode(dst.X, dst.Y))
		realpath = []
		for cord in path:
			x = self.__Graph.nodes[cord]["X"]
			y = self.__Graph.nodes[cord]["Y"]
			realpath.append((y, x))
		return realpath

	def __ToGridNode(self, x, y):
		return format(f"{x},{y}")

	def __GenrateGraph(self):

		height, width = self.__MazeParser.GetDims()
		labels = {}
		self.__Graph = nx.Graph()
		for rowIndex in range(0, width):
			for colIndex in range(0, height):
				if (self.__MazeParser.GetMatrix()[rowIndex][colIndex] == 1):
					coord = self.__ToGridNode(colIndex, rowIndex)
					# we set connectivity
					self.__Graph.add_node(coord)
					self.__Graph.nodes[coord]["X"] = colIndex
					self.__Graph.nodes[coord]["Y"] = rowIndex
				else:
					k = 0
		for node in self.__Graph.nodes:
			colIndex = self.__Graph.nodes[node]["X"]
			rowIndex = self.__Graph.nodes[node]["Y"]
			self.__AttemptToConnect(node, colIndex, rowIndex, 0, 1)
			self.__AttemptToConnect(node, colIndex, rowIndex, 0, -1)
			self.__AttemptToConnect(node, colIndex, rowIndex, -1, 0)
			self.__AttemptToConnect(node, colIndex, rowIndex, -1, 1)
			self.__AttemptToConnect(node, colIndex, rowIndex, -1, -1)
			self.__AttemptToConnect(node, colIndex, rowIndex, 1, 0)
			self.__AttemptToConnect(node, colIndex, rowIndex, 1, -1)
			self.__AttemptToConnect(node, colIndex, rowIndex, 1, 1)

	def __AttemptToConnect(self, node, colIndex, rowIndex, xFactor, yFactor):
		width, height = width, height = self.__MazeParser.GetDims()
		newColIndex = colIndex + xFactor
		newRowIndex = rowIndex + yFactor
		if (newColIndex) >= width:
			return
		if (newColIndex) < 0:
			return
		if (newRowIndex) >= height:
			return
		if (newRowIndex) < 0:
			return
		AdjNode = self.__ToGridNode(newColIndex, newRowIndex)
		if (AdjNode in self.__Graph):
			# we set connectivity
			self.__Graph.add_edge(AdjNode, node)
