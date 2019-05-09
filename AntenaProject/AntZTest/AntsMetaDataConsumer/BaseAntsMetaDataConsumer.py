from abc import ABC,abstractmethod
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.BaseTotalWorldImage import BaseTotalWorldImage
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
class BaseAntsMetaDataConsumer(ABC):
    def __init__(self,config):
        self._config=config

    @abstractmethod
    def ProcessPreRun(self,numberofsteps:int,maze:MazeFacade,aditionaldata):
        pass

    @abstractmethod
    def ProcessPreSysStep(self,step:int,worldimage:BaseTotalWorldImage, aditionaldata):
        pass

    @abstractmethod
    def ProcessAntStep(self,step:int,ant:BasicAnt,antworldimage:BaseSingleAntWorldImage,move:AntStep, aditionaldata):
        pass

    @abstractmethod
    def ProcessPostSysStep(self,step:int, worldimage:BaseTotalWorldImage, aditionaldata):
        pass

    @abstractmethod
    def ProcessPreStopRun(self,numberofsteps:int,worldimage:BaseTotalWorldImage , aditionaldata):
        pass