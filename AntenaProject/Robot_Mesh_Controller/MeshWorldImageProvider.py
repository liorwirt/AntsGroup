
from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.SimpleExample.SimpleSingleAntWorldImage import SimpleSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.SimpleExample.SimpleTotalWorldImage import SimpleTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.AlgExternalCommand import AlgExternalCommand
from AntenaProject.AntZTest.Commands.CommandsReciver import CommandsReciver
import numpy as np
class MeshWorldImageProvider(BasicWorldImageProvider):
	def __init__(self, config, maze, commandreciver:CommandsReciver):
		BasicWorldImageProvider.__init__(self,config,maze)
		self.__AntsPlannedStepDict = {}
		self.__AntsWorldImage = {}
		self.__ExploredCells = np.zeros(maze.GetDims())
		self.__CombinedMap = np.zeros(maze.GetDims())
		self.__Ants = {}
		self.__CommandsReciver=commandreciver
		self.__VisibilityRange = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "VisibilityRange", 1))
		self.__AllowedMovement = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "AllowedMovement", 1))
	def ProcessStep(self, ant: BasicAnt, step: AntStep):
		if self._Maze.MayMove(ant.CurrentPosition, step.Position, self.__AllowedMovement):
			self.__AntsPlannedStepDict[ant.ID] = (ant, step)

	def GetAntWorldImage(self, ant: BasicAnt) -> BaseSingleAntWorldImage:
		antworldimage = self.__GetPositionWorldImage(ant.CurrentPosition)
		self.__AntsWorldImage[ant.ID] = antworldimage
		return antworldimage
	def __GetPositionWorldImage(self, position: Position):
		visiblenodes = []
		self.__ExploredCells[position.Y][position.X] = 1
		leftMost, rightMost, topMost, bottomMost = self.__GetBB(position=position, radius=self.__VisibilityRange)
		for pos_x in range(leftMost, rightMost + 1):
			for pos_y in range(topMost, bottomMost + 1):
				visibleNodePosition = Position(x=pos_x, y=pos_y)
				state = self.__CombinedMap[pos_y][pos_x]
				visiblenodes.append(NodeState(NodeStateEnum(state), visibleNodePosition))
		world_image=[]
		dim_y,dim_x=self.__CombinedMap.shape
		for pos_x in range(dim_x):
			for pos_y in range(dim_y):
				visibleNodePosition = Position(x=pos_x, y=pos_y)
				state = self.__CombinedMap[pos_y][pos_x]
				world_image.append(NodeState(NodeStateEnum(state), visibleNodePosition))
		ants_with_planned_position = {}
		for id in self.__Ants:
			ants_with_planned_position[id] = self.__Ants[id].CurrentPosition
		for id in self.__AntsPlannedStepDict:
			ants_with_planned_position[id] = self.__AntsPlannedStepDict[id][1].Position

		return SimpleSingleAntWorldImage(worldImage=world_image,ants= ants_with_planned_position,visible_nodes=visiblenodes)

	def GetWorldImage(self) -> BaseTotalWorldImage:
		return SimpleTotalWorldImage(self.__AntsWorldImage, self.__CombinedMap, self.__Ants)

	def UpdatePositionsAccordingToMoves(self):
		for value in self.__AntsPlannedStepDict.values():
			step = value[1]
			ant = value[0]
			ant.UpdatePosition(step.Position)
			self.__Ants[ant.ID] = ant
			self.__UpdateExploredStepsPerAnt(step.Position)

		self.__GenrateCombinedMap()
		self.__AntsPlannedStepDict.clear()
		commands = self.__CommandsReciver.GetCommands()
		for command in commands:
			self.__HandleCommand(command)

	def __HandleCommand(self, command: AlgExternalCommand):
		# TODO HandleCommand
		pass

	def __GetBB(self, radius: int, position: Position):
		leftMost = max(0, position.X -radius)
		rightMost = min(self._Maze.GetDims()[1] - 1, position.X + radius)

		topMost = max(0, position.Y - radius)
		bottomMost = min(self._Maze.GetDims()[0] - 1, position.Y + radius)
		return leftMost, rightMost, topMost, bottomMost

	def __UpdateExploredStepsPerAnt(self, position: Position):
		self.__ExploredCells[position.Y][position.X] = 1
		leftMost, rightMost, topMost, bottomMost = self.__GetBB(position=position, radius=self.__VisibilityRange)

		for pos_x in range(leftMost, rightMost + 1):
			for pos_y in range(topMost, bottomMost + 1):
				self.__ExploredCells[pos_y][pos_x] = 1

	def __GenrateCombinedMap(self):

		[height, width] = self.__ExploredCells.shape
		for pos_x in range(0, width):
			for pos_y in range(0, height):
				if (self.__ExploredCells[pos_y][pos_x] == 0):
					self.__CombinedMap[pos_y][pos_x] = NodeStateEnum.UnExplored
				else:
					if (self._Maze.IsObs(Position(x=pos_x, y=pos_y))):
						self.__CombinedMap[pos_y][pos_x] = NodeStateEnum.Obs
					else:
						self.__CombinedMap[pos_y][pos_x] = NodeStateEnum.Clear
		for ant in self.__Ants.values():
			self.__CombinedMap[ant.CurrentPosition.Y][ant.CurrentPosition.X] = NodeStateEnum.Ant
    #def __get_planned_positions(self):
       #
        #
        # return ants_with_planned_position
