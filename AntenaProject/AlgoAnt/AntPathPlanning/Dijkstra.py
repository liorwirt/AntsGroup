import numpy as np
import heapq
from AntenaProject.Common.AntsBasicStructures.Position import Position


def Dijkstra(InputGrid: np.array, Source: Position):
	WeightGrid = np.full(InputGrid.shape, np.inf)
	WeightGrid[Source.X, Source.Y] = 0.0
	VisitedNodes = []
	# maximum indexes in the matrix
	Width, Height = InputGrid.shape

	q = []
	TieBreaker = 0
	heapq.heappush(q, (WeightGrid[Source.X, Source.Y], TieBreaker, Source))
	TieBreaker += 1
	while len(q) > 0:
		CurrentWeight, _, CurrentNode = heapq.heappop(q)
		if CurrentNode in VisitedNodes:
			continue

		VisitedNodes.append(CurrentNode)

		for Neighbour in GetNeighbours(CurrentNode, Width, Height):
			if InputGrid[Neighbour.X, Neighbour.Y] is np.inf:
				continue
			if WeightGrid[Neighbour.X, Neighbour.Y] > CurrentWeight + InputGrid[Neighbour.X, Neighbour.Y]:
				WeightGrid[Neighbour.X, Neighbour.Y] = CurrentWeight + InputGrid[Neighbour.X, Neighbour.Y]

				heapq.heappush(q, (WeightGrid[Neighbour.X, Neighbour.Y], TieBreaker, Neighbour))
				TieBreaker += 1
	return WeightGrid


def GetNeighbours(Source: Position, Width: int, Height: int) -> list:
	result = []
	if Source.X > 0:
		result.append(Position(Source.X - 1, Source.Y))
	if Source.Y > 0:
		result.append(Position(Source.X, Source.Y - 1))
	if Source.X < Width - 1:
		result.append(Position(Source.X + 1, Source.Y))
	if Source.Y < Height - 1:
		result.append(Position(Source.X, Source.Y + 1))

	return result
