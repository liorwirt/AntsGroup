from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.SimpleExample.ExampleAnts.SimpleRandomMemoryLessAnt import SimpleRandomMemoryLessAnt
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Common.AntsBasicStructures.Position import Position

class SimpleAntProducer(BasicAntProducer):

    def __init__(self,config:BaseConfigProvider,initialposition:Position):
        BasicAntProducer.__init__(self,config)
        self.__AntsList = []
        self.__Counter = 0
        self.__InitialPosition=initialposition

    def CreateAnts(self):
        numbertoproduce=int(self._Config.GetConfigValueForSectionAndKey("SimpleAnt","NumToProduce",100))
        for id in range(numbertoproduce):
            ant=SimpleRandomMemoryLessAnt(id,self._Config)
            ant.UpdatePosition(position=Position(x=self.__InitialPosition.X,y=self.__InitialPosition.Y))

            self.__AntsList.append(ant)


    def _StopIteration(self) -> bool:
        if(self.__Counter>=len(self.__AntsList)-1):

            return True
        return False

    def _NextAnt(self) -> SimpleRandomMemoryLessAnt:

        if self._StopIteration():
            return self.__AntsList[ self.__Counter-1]

        ant= self.__AntsList[self.__Counter]
        self.__Counter += 1
        return ant
    def __iter__(self):
        return self

    def __next__(self) -> SimpleRandomMemoryLessAnt:
        if self._StopIteration():
            self.__Counter = 0
            raise StopIteration
        else:
            return self._NextAnt()

    def added_ants(self, num_of_ants_produced, world_image):
        return []