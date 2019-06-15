import numpy as np
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
import unittest
from AntenaProject.Common.AntsBasicStructures.Position import Position
import copy


def isInRange(combined_map, radius, position1, position2):
	return isInRadius(radius, position1, position2) and isLOS(combined_map, position1, position2)


def isInRadius(radius, position1, position2):
	# Function returns true if the distance between the points is smaller than the radius
	# Points: expecting two positions (class position)
	dist = np.linalg.norm([position2.X - position1.X, position2.Y - position1.Y])
	is_in_radius = dist <= radius
	return is_in_radius


def isLOS(combined_map, position1, position2):
	# Function returns true if there is a there is a continuous LOS between the two points (LOS not blocked)
	# Assumption: LOS passes between two diagonally touching points
	# Points: expecting lists with two elements
	x0 = copy.deepcopy(position1.X)
	y0 = copy.deepcopy(position1.Y)
	x1 = copy.deepcopy(position2.X)
	y1 = copy.deepcopy(position2.Y)
	dx = x1 - x0
	dy = y1 - y0
	f = 0
	if dy < 0:
		dy = -dy
		sy = -1
	else:
		sy = 1
	if dx < 0:
		dx = -dx
		sx = -1
	else:
		sx = 1
	if dx >= dy:
		while x0 != x1:
			f = f + dy
			if f >= dx:
				if isBlocked(combined_map[int(x0 + (sx - 1) / 2), int(y0 + (sy - 1) / 2)]):
					return False
				y0 = y0 + sy
				f = f - dx
			if f != 0 and isBlocked(combined_map[int(x0 + (sx - 1) / 2), int(y0 + (sy - 1) / 2)]):
				return False
			if dy == 0 and isBlocked(combined_map[int(x0 + (sx - 1) / 2), int(y0)]) and isBlocked(
					combined_map[int(x0 + (sx - 1) / 2), int(y0 - 1)]):
				return False
			x0 = x0 + sx
	else:
		while y0 != y1:
			f = f + dx
			if f >= dy:
				if isBlocked(combined_map[int(x0 + (sx - 1) / 2), int(y0 + (sy - 1) / 2)]):
					return False
				x0 = x0 + sx
				f = f - dy
			if f != 0 and isBlocked(combined_map[int(x0 + (sx - 1) / 2), int(y0 + (sy - 1) / 2)]):
				return False
			if dy == 0 and isBlocked(combined_map[int(x0), int(y0 + (sy - 1) / 2)]) and isBlocked(
					combined_map[int(x0 - 1), int(y0 + (sy - 1) / 2)]):
				return False
			y0 = y0 + sy
	return True


def isBlocked(currentPointType):
	# A point in grid is considered blocked if it is unexplored or it is an obstacle
	return int(currentPointType) == NodeStateEnum.UnExplored or int(currentPointType) == NodeStateEnum.Obs


def FakeMazeCreator(dimensions):
	maze = np.ones((dimensions, dimensions))
	maze[6, 8] = NodeStateEnum.Obs
	maze[11, 11] = NodeStateEnum.Obs
	maze[2, 3] = NodeStateEnum.Obs
	maze[2, 4] = NodeStateEnum.Obs
	maze[2, 5] = NodeStateEnum.Obs
	maze[2, 6] = NodeStateEnum.Obs
	maze[2, 7] = NodeStateEnum.Obs
	maze[11, 10] = NodeStateEnum.Obs
	return maze


class TestUtilFunctions(unittest.TestCase):
	def test_isInRange_Method(self):
		position1 = Position(3, 5)
		position2 = Position(8, 10)
		radius = 2
		in_radius = isInRadius(radius, position1, position2)
		fake_maze = FakeMazeCreator(12)
		is_los = isLOS(fake_maze, position1, position2)
		print("In range: " + str(isInRange(fake_maze, radius, position1, position2)))


if __name__ == '__main__':
	unittest.main()
