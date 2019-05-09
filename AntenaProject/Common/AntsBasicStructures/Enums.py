from enum import IntEnum


class NodeStateEnum(IntEnum):
    UnExplored=0,
    Clear=1,
    Obs=2,
    Ant=3,