class Position(object):
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    @property
    def X(self):
        return self.__x

    @property
    def Y(self):
        return self.__y


    def __str__(self):
        return format(f" x {self.__x} y {self.__y}")

    def __eq__(self, other):
        return   self.__y==other.Y and self.__x==other.X

    @staticmethod
    def GetEmptyPoistion():
        return Position(-1,-1)