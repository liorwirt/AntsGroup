from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
class NodeState(object):
    def __init__(self,nodestate:NodeStateEnum,position:Position):
        self.__nodeState=nodestate
        self.__position=position

    @property
    def Position(self):
        return self.__position


    @property
    def NodeState(self):
        return self.__nodeState

    def __str__(self):
        return format(f"Node State {self.__nodeState}  position [ {self.__position}]")

    def __eq__(self, other):
        return self.__nodeState==other.NodeState and self.__position==other.Position