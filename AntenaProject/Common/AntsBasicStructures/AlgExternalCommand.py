from AntenaProject.Common.AntsBasicStructures.Enums import AlgCommandEnum
from AntenaProject.Common.AntsBasicStructures.Position import Position

class AlgExternalCommand(object):
    def __init__(self,position:Position,command:AlgCommandEnum):
        self._Command=command
        self._Position=position


    @property
    def Command(self):
        return self._Command

    @property
    def Position(self):
        return self._Position

