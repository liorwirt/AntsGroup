from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.AlgoAnt.AlgoAnt import AlgoAnt
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Common.AntsBasicStructures.Position import Position

class AlgoAntProducer(BasicAntProducer):

    def __init__(self,config:BaseConfigProvider,initialposition:Position):
        BasicAntProducer.__init__(self,config)
        self.__AntsList = []
        self.__Counter = 0
        self.__InitialPosition=initialposition

    def CreateAnts(self):
        numbertoproduce=int(self._Config.GetConfigValueForSectionAndKey("AlgoAnt", "NumToProduce", 10))
        for id in range(numbertoproduce):
            startingPosition = Position(x=self.__InitialPosition.X, y=self.__InitialPosition.Y)
            ant = AlgoAnt(id, self._Config, startingPosition)
            self.__AntsList.append(ant)


    def _StopIteration(self) -> bool:
        if(self.__Counter>=len(self.__AntsList)-1):

            return True
        return False

    def _NextAnt(self) -> AlgoAnt:

        if self._StopIteration():
            return self.__AntsList[ self.__Counter-1]

        ant= self.__AntsList[self.__Counter]
        self.__Counter += 1
        return ant
    def __iter__(self):
        return self

    def __next__(self) -> AlgoAnt:
        if self._StopIteration():
            self.__Counter = 0
            raise StopIteration
        else:
            return self._NextAnt()