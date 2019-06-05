from AntenaProject.Common.AntsBasicStructures.Position import Position
class AntStep(object):
    def __init__(self,antid,position:Position):
        self.__antid=antid
        self.__position=position

    @property
    def Position(self):
        return self.__position


    @property
    def AntId(self):
        return self.__antid

    def __str__(self):
        return format(f"antid {self.__antid}  position[ {self.__position}]")

    def __eq__(self, other):
        return self.__antid==other.AntId and self.__position==other.Position