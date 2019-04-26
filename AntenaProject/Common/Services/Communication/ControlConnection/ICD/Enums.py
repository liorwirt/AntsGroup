from enum import Enum
class ServiceStatusEnum(Enum):
    Stopped=1
    Starting=2
    Started=3
    Stoping=4
    Error=5

class ControlCommTypesEnum(Enum):
    Dummy=1
    ZMQ=2

