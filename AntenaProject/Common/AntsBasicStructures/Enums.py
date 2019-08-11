from enum import IntEnum

class NodeStateEnum(IntEnum):
    UnExplored=1,
    Clear=0,
    Obs=2,
    Ant=3,


class AntType(IntEnum):
    Scout = 0,
    Transmission = 1,


class CellWeights:
    UnexploredCell = 1.0
    ExploredCell = 2.0
