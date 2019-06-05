from typing import Tuple, Dict

from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt, Position, BaseSingleAntWorldImage, AntStep


class AlgoAnt(BasicAnt):

    def __init__(self):
        pass

    @property

    def UpdatePosition(self, position: Position):
        super().UpdatePosition(position)

    def GetStep(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[AntStep, Dict]:
        return super().GetStep(antworldstate)

    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
        pass
