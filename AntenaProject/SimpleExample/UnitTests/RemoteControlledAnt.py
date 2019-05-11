from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
import numpy as np
import random

class RemoteControlledAnt(BasicAnt):
    def SetStep(self,step:Position):
        self.__Step=step
    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage):
        return self.__Step,{}