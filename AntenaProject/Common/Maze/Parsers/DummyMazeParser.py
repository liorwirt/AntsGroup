import numpy as np
from AntenaProject.Common.Maze.Parsers.BaseMazeParser import BaseMazeParser
from AntenaProject.Common.AntsBasicStructures.Position import Position
class DummyMazeParser(BaseMazeParser):


    def GetMatrix(self)->np.ndarray:
        return None

    def GetEnterence(self):
        return None

    def GetExits(self):
        return None

    def GetDims(self):
        return (0,0)

    def GetName(self):
        return "Dummy"