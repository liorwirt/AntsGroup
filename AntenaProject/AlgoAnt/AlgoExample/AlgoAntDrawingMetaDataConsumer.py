from AntenaProject.AntZTest.AntsMetaDataConsumer.BaseAntsMetaDataConsumer import BaseAntsMetaDataConsumer
from AntenaProject.Common.AntsBasicStructures.Enums import ExpandedNodeStateEnum, AntType
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.AntZTest.MazeDrawing.DrawMaze import DrawMaze

import numpy as np


class AlgoAntDrawingMetaDataConsumer(BaseAntsMetaDataConsumer):
    def __init__(self, config):
        BaseAntsMetaDataConsumer.__init__(self, config)
        self.__mazeDrawing = DrawMaze()

    def ProcessPreRun(self, numberofsteps, maze, additionaldata):
        pass

    def ProcessPreSysStep(self, step, worldimage: BaseTotalWorldImage, additionaldata):
        pass

    def ProcessAntStep(self, step, ant: BasicAnt, antworldimage, move, additionaldata):
        pass

    def ProcessPostSysStep(self, step, worldimage: BaseTotalWorldImage, additionaldata):
        completeworld = np.copy(worldimage.WorldMatrix)
        AntList = worldimage.Ants().values()
        for ant in AntList:
            if ant.Type() == AntType.Scout:
                completeworld[ant.CurrentPosition.Y, ant.CurrentPosition.X] = ExpandedNodeStateEnum.ScoutAnt
            else:
                completeworld[ant.CurrentPosition.Y, ant.CurrentPosition.X] = ExpandedNodeStateEnum.TransmissionAnt

        self.__mazeDrawing.DrawMazeState(completeworld)

    def ProcessPreStopRun(self, numberofsteps, worldimage: BaseTotalWorldImage, additionaldata):
        pass
