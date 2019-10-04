from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.AntZTest.MazeDrawing.DrawMaze import DrawMaze
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade

from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
import numpy as np
import os
class DrawingMetaDataConsumer(BaseAntsMetaDataConsumer):
    def __init__(self,config,folder,enterence:Position=Position.GetEmptyPosition()):
        BaseAntsMetaDataConsumer.__init__(self,config)
        self.__enterence=enterence
        self.__mazeDrawing=DrawMaze(config,folder)
    def ProcessPreRun(self,numberofsteps,maze,aditionaldata):
      pass
    def ProcessPreSysStep(self,step,worldimage:BaseTotalWorldImage, aditionaldata):
       pass
    def ProcessAntStep(self,step,ant:BasicAnt,antworldimage,move,aditionaldata):
        pass
    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        completeworld=np.copy(worldimage.WorldMatrix)
        if("connectivity_lines" in aditionaldata):
            connectivity_lines=aditionaldata["connectivity_lines"]
            for connectivty_line in connectivity_lines:
                for point in connectivty_line:
                    completeworld[point.Y][point.X]=4
        completeworld[self.__enterence.Y][self.__enterence.X]=5
        self.__mazeDrawing.DrawMazeState(completeworld,step)
    def ProcessPreStopRun(self,numberofsteps,worldimage:BaseTotalWorldImage , aditionaldata):
        pass

