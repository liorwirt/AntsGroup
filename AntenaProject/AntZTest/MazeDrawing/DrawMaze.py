import matplotlib.pyplot as plt
import matplotlib.colors
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
import numpy as np
import time
from matplotlib.pyplot import plot, ion, show, imshow
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
import matplotlib.animation as animation

import os.path
class DrawMaze(object):
    def __init__(self,config,folder=None):
        self.__save_images=bool(int(config.GetConfigValueForSectionAndKey("MazeDraw", "SaveImages", 0)))
        self.__folder=folder
        colorsdata = []

        colorsdata.append("silver")
        colorsdata.append("white")
        colorsdata.append("black")
        colorsdata.append("green")
        colorsdata.append("magenta")#comm
        colorsdata.append("blue")  # comm

        self.__ax = None
        self.__cmap = matplotlib.colors.LinearSegmentedColormap.from_list("Maze", colorsdata, N=6)

    def DrawMazeState(self, maze: np.matrix,step=0):
        dimensions = maze.shape
        plt.pcolormesh(maze, cmap=self.__cmap)
        plt.axes().set_aspect('equal')  # set the x and y axes to the same scale
        plt.xticks([])  # remove the tick marks by setting to an empty list
        plt.yticks([])  # remove the tick marks by setting to an empty list
        if (not plt.axes().yaxis_inverted()):
            plt.axes().invert_yaxis()  # invert the y-axis so the first row of data is at the top

        plt.show(block=False)
        plt.pause(0.001)
        if self.__save_images:
            file_name=os.path.join(self.__folder,format(f"Step_{step}.png"))
            plt.savefig(file_name)

