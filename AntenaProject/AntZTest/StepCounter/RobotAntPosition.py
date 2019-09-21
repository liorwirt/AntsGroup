from dataclasses import dataclass
from AntenaProject.AntZTest.StepCounter.Enums import DirectionsEnum
from AntenaProject.AntZTest.StepCounter.Enums import StepEnum

@dataclass
class RobotAntPosition:
    direction: DirectionsEnum
    X: int
    Y:int