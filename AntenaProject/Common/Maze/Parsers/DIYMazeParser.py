import numpy as np
from typing import List
from AntenaProject.Common.Maze.Parsers.BaseMazeParser import BaseMazeParser
from AntenaProject.Common.AntsBasicStructures.Position import Position

class DIYMazeParser(BaseMazeParser):

    def __init__(self,dimensions):
        self.__dimensions=dimensions
        self.__Maze=np.ones((dimensions,dimensions))

        self.__Enterance = Position(0, 0)
        self.__Exits = [Position(0, 0)]
    def SetExits(self,exits:List[Position]):
        self.__Exits = exits
    def SetEntrence(self,entrence:Position):
        self.__Enterance = entrence

    def SetObs(self,osticals:List[Position]):
        self.__Maze = np.ones(( self.__dimensions,  self.__dimensions))
        for obstical in osticals:
            self.__Maze[obstical.Y][obstical.X]=0

    def GetMatrix(self)->np.ndarray:
        return self.__Maze

    def GetEnterence(self):
        return self.__Enterance

    def GetExits(self):
        return self.__Exits

    def GetDims(self):
        return self.__Maze.shape


    def IsObs(self,position:Position)->bool:
        return  self.__Maze[position.Y][position.X]==0

    def GetName(self):
        return "DIY Testing Maze"