from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.AntsBasicStructures.NodeState import NodeState

class SimpleSingleAntWorldImage(BaseSingleAntWorldImage):
    def __init__(self,visiblenodes):
        self.__VisibleNodes=visiblenodes
    @property
    def VisibleNodes(self):
        return self.__VisibleNodes