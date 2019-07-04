import numpy as np
import heapq
from AntenaProject.Common.AntsBasicStructures.Position import Position


def Dijkstra(InputGrid: np.array, Source: Position):
	WeightGrid = np.full(InputGrid.shape, np.inf)
	WeightGrid[Source.Y, Source.X] = 0.0
	VisitedNodes = []
	# maximum indexes in the matrix
	Width, Height = InputGrid.shape

	q = []
	TieBreaker = 0
	heapq.heappush(q, (WeightGrid[Source.Y, Source.X], TieBreaker, Source))
	TieBreaker += 1
	while len(q) > 0:
		CurrentWeight, _, CurrentNode = heapq.heappop(q)
		if CurrentNode in VisitedNodes:
			continue

		VisitedNodes.append(CurrentNode)

		for Neighbour in GetNeighbours(CurrentNode, Width, Height):
			if InputGrid[Neighbour.Y, Neighbour.X] is np.inf:
				continue
			if WeightGrid[Neighbour.Y, Neighbour.X] > CurrentWeight + InputGrid[Neighbour.Y, Neighbour.X]:
				WeightGrid[Neighbour.Y, Neighbour.X] = CurrentWeight + InputGrid[Neighbour.Y, Neighbour.X]

				heapq.heappush(q, (WeightGrid[Neighbour.Y, Neighbour.X], TieBreaker, Neighbour))
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
