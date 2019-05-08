import numpy as np
from AntenaProject.Common.Maze.Parsers.BaseMazeParser import BaseMazeParser
from AntenaProject.Common.AntsBasicStructures.Position import Position

class FixedMazeParser(BaseMazeParser):

    def __init__(self):
        self.__Maze=np.ones((5,5))
        self.__Maze[0][1]=0
        self.__Maze[2][1] = 0
        self.__Maze[0][3] = 0
        self.__Maze[2][3] = 0
        self.__Enterence=Position(0,0)
        self.__Exits = [Position(4, 4),Position(4,2)]
    def GetMatrix(self)->np.ndarray:
        return self.__Maze

    def GetEnterence(self):
        return self.__Enterence

    def GetExits(self):
        return self.__Exits

    def GetDims(self):
        return (5,5)


    def IsObs(self,position:Position)->bool:
        return  self.__Maze[position.Y][position.X]==0

    def GetName(self):
        return "Fixed Testing Maze"