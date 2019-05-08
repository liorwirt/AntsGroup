import numpy as np
from AntenaProject.Common.Maze.Parsers.BaseMazeParser import BaseMazeParser
import os.path
from AntenaProject.Common.AntsBasicStructures.Position import Position

class FileMazeParser(BaseMazeParser):

    def __init__(self,filename):
        if not os.path.isfile(filename):
            raise Exception(format(f"file {filename} not found"))
        self.__Exits=[]
        self.__map_2_occupancy_map(filename)
        self.__Name=format(f"file maze {filename}")


    def GetMatrix(self)->np.ndarray:
        return self.__Maze

    def GetEnterence(self):
        return self.__Enterence

    def GetExits(self):
        return self.__Exits

    def GetDims(self):
        return self.__Maze.shape

    def GetName(self):
        return self.__Name

    def IsObs(self,position:Position)->bool:
        return  self.__Maze[position.Y][position.X]==0




    def __map_2_occupancy_map(self,filename):
        map_planning = np.loadtxt(filename, dtype="str")


        enterindexs= np.where(map_planning =='S')
        if len(enterindexs[0]) == 0:
            raise Exception(format(f"file {filename} no enterence found"))
        if len(enterindexs[0])>1:
            raise Exception(format(f"file {filename} several enterences found"))
        self.__Enterence= Position(enterindexs[0], enterindexs[1])

        exitindexs= np.where(map_planning =='F')
        if len(exitindexs[0]) == 0:
            raise Exception(format(f"file {filename} no exits found"))
        exittupels = list(zip(exitindexs[0], exitindexs[1]))

        for tup in exittupels:
            self.__Exits.append(Position(tup[0],tup[1]))


        ''' Takes the matrix and converts it into a float array '''
        map_arr = np.copy(map_planning)
        map_arr[map_arr == 'O'] = 0
        map_arr[map_arr == 'E'] = 1
        map_arr[map_arr == 'S'] = 1
        map_arr[map_arr == 'F'] = 1
        self.__Maze = map_arr.astype(np.int)