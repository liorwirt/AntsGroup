import numpy as np
from AntenaProject.Common.Maze.Parsers.BaseMazeParser import BaseMazeParser
import os.path


class FileMazeParser(BaseMazeParser):

    def __init__(self,filename):
        if not os.path.isfile(filename):
            raise Exception(format(f"file {filename} not found"))
        self.__map_2_occupancy_map(filename)

    def GetMatrix(self)->np.ndarray:
        return self.__Maze

    def GetEnterence(self):
        return self.__Enterence

    def GetExits(self):
        return self.__Exits

    def GetDims(self):
        return self.__Maze.shape





    def __map_2_occupancy_map(self,filename):
        map_planning = np.loadtxt(filename, dtype="str")


        enterindexs= np.where(map_planning =='S')
        if len(enterindexs[0]) == 0:
            raise Exception(format(f"file {filename} no enterence found"))
        if len(enterindexs[0])>1:
            raise Exception(format(f"file {filename} several enterences found"))
        self.__Enterence= (enterindexs[0], enterindexs[1])

        exitindexs= np.where(map_planning =='F')
        if len(exitindexs[0]) == 0:
            raise Exception(format(f"file {filename} no exits found"))
        self.__Exits = list(zip(exitindexs[0], exitindexs[1]))

        ''' Takes the matrix and converts it into a float array '''
        map_arr = np.copy(map_planning)
        map_arr[map_arr == 'O'] = 0
        map_arr[map_arr == 'E'] = 1
        map_arr[map_arr == 'S'] = 1
        map_arr[map_arr == 'F'] = 1
        self.__Maze = map_arr.astype(np.int)