from abc import ABC, abstractmethod
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.AntStep import AntStep
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from typing import Dict, Tuple


class BasicAnt(ABC):
    def __init__(self, id: int, config):
        self._Config = config
        self._ID = id
        self._CurrentPosition = Position.GetEmptyPosition()

    @property
    def ID(self):
        return self._ID

    @property
    def CurrentPosition(self):
        return self._CurrentPosition

    @abstractmethod
    def _internalGetStep(self, antworldstate) -> Tuple[Position, Dict]:
        pass

    def UpdatePosition(self, position: Position):
        self._CurrentPosition = position

    def GetStep(self, antworldstate) -> Tuple[AntStep, Dict]:
        position, additionaldata = self._internalGetStep(antworldstate)
        return AntStep(self._ID, position), additionaldata

    def Type(self):
        return NodeStateEnum.Ant
