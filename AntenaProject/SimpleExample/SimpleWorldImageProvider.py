from AntenaProject.Common.AntsBasicStructures.BasicWorldImageProvider import BasicWorldImageProvider
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.SimpleExample.SimpleSingleAntWorldImage import SimpleSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.SimpleExample.SimpleTotalWorldImage import SimpleTotalWorldImage
import numpy as np



class SimpleWorldImageProvider(BasicWorldImageProvider):

    def __init__(self,config,maze):
        BasicWorldImageProvider.__init__(self,config,maze)
        self.__AntsPlannedStepDict={}
        self.__AntsWorldImage = {}
        self.__ExploredCells=np.zeros(maze.GetDims())
        self.__CombinedMap = np.zeros(maze.GetDims())
        self.__Ants={}
        self.__VisibilityRange = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "VisibilityRange", 1))
        self.__AllowedMovement = int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt", "AllowedMovement", 1))

    def ProcessStep(self, ant: BasicAnt, step: AntStep):
            if self._Maze.MayMove(ant.CurrentPosition,step.Position,self.__AllowedMovement):
                self.__AntsPlannedStepDict[ant.ID]=(ant,step)


    def GetAntWorldImage(self, ant: BasicAnt) -> BaseSingleAntWorldImage:
        antsworldimage=self.__GetPositionWorldImage(ant.CurrentPosition)
        self.__AntsWorldImage[ant.ID]=antsworldimage
        return antsworldimage

    def __GetPositionWorldImage(self,position:Position):
        visiblenodes=[]
        self.__ExploredCells[position.Y][position.X] = 1
        leftMost = max(0, position.X - int(np.floor(self.__VisibilityRange / 2)))
        rightMost = min(self._Maze.GetDims()[1],  int(position.X + np.floor(self.__VisibilityRange / 2)))

        topMost = max(0, position.Y -  int(np.floor(self.__VisibilityRange / 2)))
        bottomMost = min(self._Maze.GetDims()[0],  int(position.Y +np.floor(self.__VisibilityRange / 2)))
        for pos_x in range(leftMost, rightMost+1):
            for pos_y in range(topMost, bottomMost+1):
                if(self.__ExploredCells[position.Y][position.X]==0):
                    visiblenodes.append(NodeState(NodeStateEnum.UnExplored,Position(x=pos_x,y=pos_y)))
                else:
                    if(self._Maze.IsObs(position)):
                        visiblenodes.append(NodeState(NodeStateEnum.Obs, Position(x=pos_x, y=pos_y)))
                    else:
                        visiblenodes.append(NodeState(NodeStateEnum.Clear, Position(x=pos_x, y=pos_y)))


        return SimpleSingleAntWorldImage(visiblenodes)

    def GetWorldImage(self) -> BaseTotalWorldImage:
        return SimpleTotalWorldImage( self.__AntsWorldImage,self.__CombinedMap)

    def UpdatePositionsAccordingToMoves(self):
        for value in self.__AntsPlannedStepDict.values():
            step=value[1]
            ant=value[0]
            ant.UpdatePosition(step.Position)
            self.__Ants[ant.ID]=ant
            self.__UpdateExploredStepsPerAnt(step.Position)
            self.__GenrateCombinedMap()

        self.__AntsPlannedStepDict.clear()
    def __UpdateExploredStepsPerAnt(self,position:Position):
        self.__ExploredCells[position.Y][position.X]=1
        leftMost=max(0,position.X- int(np.floor(self.__VisibilityRange/2)))
        rightMost = min(self._Maze.GetDims()[1],  int(position.X + np.floor(self.__VisibilityRange / 2)))

        topMost = max(0, position.Y -  int(np.floor(self.__VisibilityRange / 2)))
        bottomMost = min(self._Maze.GetDims()[0],  int(position.Y+ np.floor(self.__VisibilityRange / 2)))

        for pos_x in range(leftMost,rightMost+1):
            for pos_y in range (topMost,bottomMost+1):
                self.__ExploredCells[position.Y][position.X] = 1

    def __GenrateCombinedMap(self):
        #TODO add refrenceOfAnts
        [height,width]=self.__ExploredCells.shape
        for idx_X in range(0,width):
            for idx_Y in range(0,height):
                if(self.__ExploredCells[idx_Y][idx_X]==0):
                    self.__CombinedMap[idx_Y][idx_X]=NodeStateEnum.UnExplored
                else:
                    if (self._Maze.IsObs(Position(x=idx_X,y=idx_Y))):
                        self.__CombinedMap[idx_Y][idx_X] = NodeStateEnum.Obs
                    else:
                        self.__CombinedMap[idx_Y][idx_X]=NodeStateEnum.Clear
        for ant in self.__Ants.values():
            self.__CombinedMap[ant.CurrentPosition.Y][ant.CurrentPosition.X] = NodeStateEnum.Ant
