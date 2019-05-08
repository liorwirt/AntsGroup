from enum import Enum


class NodeStateEnum(Enum):
    UnExplored=0,
    Clear=1,
    Obs=2,
    Ant=3,