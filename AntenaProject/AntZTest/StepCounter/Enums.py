from enum import IntEnum


class StepEnum(IntEnum):
    Forward=0,
    Back = 1,
    TurnLeft=2,
    TurnRight=3,
    NoStep=4
class DirectionsEnum(IntEnum):
    North=0,
    South=1,
    East=2,
    West=3,