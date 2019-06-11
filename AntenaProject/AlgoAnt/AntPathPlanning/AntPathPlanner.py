import numpy as np
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.Position import Position


# from dijkstra import...

class AntPathPlanner():
    def __init__(self, WorldImage: BaseSingleAntWorldImage):
        self.__WorldImage = WorldImage
        # self.__CurrentDestination = CurrentDestination
        # receive list of weights

    def PlanPath(self):
        pass
        # convert world image into weighted matrix
        # run dijkstra on matrix
        # choose a destination
        # decide if we want to switch destinations (we might have arrived at the current one)
        # calculate a path to the destination
        # return the destination


    def __ConvertWorldImageToWeightedMatrix(worldImage, safetyRadius: int, cellTypeWeights):
        resultMatrix = np.zeros(worldImage.matrix.shape)

        resultMatrix = np.where(worldImage.matrix  == 'blocked', np.inf, cellTypeWeights['free'])



    def __ChooseNextDestination(self, NewDestination: Position):
        pass

    def __CalculatePathToDestination(self):
        pass
