from typing import Tuple, Dict
import numpy as np

from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt, Position, BaseSingleAntWorldImage, AntStep


class AlgoAnt(BasicAnt):

    def __init__(self, id: int, config, position: Position):
        super().__init__(id, config)
        super().UpdatePosition(position)

    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage) -> Tuple[Position, Dict]:
        pass

