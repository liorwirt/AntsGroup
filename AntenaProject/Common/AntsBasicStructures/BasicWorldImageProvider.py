from abc import ABC,abstractmethod
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage

class BasicWorldImageProvider(ABC):
    def __init__(self,config,maze):
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

    def GetAntPosition(self,ant:BasicAnt)->Position:
        pass