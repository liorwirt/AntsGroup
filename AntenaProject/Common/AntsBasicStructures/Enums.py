from enum import IntEnum


class NodeStateEnum(IntEnum):
    Clear = 0,
    UnExplored = 1,
    Obs = 2,
    Ant = 3,


class ExpandedNodeStateEnum(IntEnum):
    Clear = 0,
    UnExplored = 1,
    Obs = 2,
    ScoutAnt = 3,
    TransmissionAnt = 4,


class AntType(IntEnum):
    Scout = 0,
    Transmission = 1,


class CellWeights:
    UnexploredCell = 1.0
    ExploredCell = 2.0


class AlgCommandEnum(IntEnum):
    Clear = 0,
    NotRelevent = 1,
    Blocked = 2,
    Priority = 3
