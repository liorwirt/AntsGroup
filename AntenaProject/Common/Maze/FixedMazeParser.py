from abc import ABC, abstractmethod
import numpy as np
from AntenaProject.Common.Maze.BaseMazeParser import BaseMazeParser

class FixedMazeParser(BaseMazeParser):

    def __init__(self):
        self.__Maze=np.ones((5,5))
        self.__Maze[0][1]=0
        self.__Maze[2][1] = 0
        self.__Maze[0][3] = 0
        self.__Maze[2][3] = 0
        self.__Enterence=(0,0)
        self.__Exits = [(4, 4),(4,2)]
    def GetMatrix(self)->np.ndarray:
        return self.__Maze

    def GetEnterence(self):
        return self.__Enterence

    def GetExits(self):
        return self.__Exits

    def GetDims(self):
        return (5,5)