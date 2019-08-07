from enum import IntEnum


class NodeStateEnum(IntEnum):
    UnExplored=0,
    Clear=1,
    Obs=2,
    Ant=3,

class AlgCommandEnum(IntEnum):
    Clear=0,
    NotRelevent=1,
    Blocked=2,
    Priority=3