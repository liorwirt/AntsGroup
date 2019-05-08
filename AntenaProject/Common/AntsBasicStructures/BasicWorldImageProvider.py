from abc import ABC,abstractmethod
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider

class BasicWorldImageProvider(ABC):
    def __init__(self,config:BaseConfigProvider,maze:MazeFacade):
        self._Maze=maze
        self._Config=config
    @abstractmethod
    def ProcessStep(self,ant:BasicAnt,step:AntStep):
        pass

    @abstractmethod
    def GetAntWorldImage(self, ant: BasicAnt)->BaseSingleAntWorldImage:
        pass

    @abstractmethod
    def GetWorldImage(self)->BaseTotalWorldImage:
        pass

    @abstractmethod
    def UpdatePositionsAccordingToMoves(self):
        pass


