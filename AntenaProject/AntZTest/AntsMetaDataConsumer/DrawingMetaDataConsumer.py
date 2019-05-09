from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.AntZTest.MazeDrawing.DrawMaze import DrawMaze
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
import numpy as np
import os
class DrawingMetaDataConsumer(BaseAntsMetaDataConsumer):
    def __init__(self,config):
        BaseAntsMetaDataConsumer.__init__(self,config)
        self.__mazeDrawing=DrawMaze()
    def ProcessPreRun(self,numberofsteps,maze,aditionaldata):
      pass
    def ProcessPreSysStep(self,step,worldimage:BaseTotalWorldImage, aditionaldata):
       pass
    def ProcessAntStep(self,step,ant:BasicAnt,antworldimage,move,aditionaldata):
        pass
    def ProcessPostSysStep(self,step, worldimage:BaseTotalWorldImage, aditionaldata):
        completeworld=np.copy(worldimage.WorldMatrix)
        self.__mazeDrawing.DrawMazeState(completeworld)
    def ProcessPreStopRun(self,numberofsteps,worldimage:BaseTotalWorldImage , aditionaldata):
        pass

