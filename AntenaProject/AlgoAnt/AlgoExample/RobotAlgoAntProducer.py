from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.AlgoAnt.AlgoAnt import AlgoAnt
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import AntType
from AntenaProject.AntZTest.RobotCommuincation.ServerComm import ServerComm

class RobotAlgoAntProducer(BasicAntProducer):

    def __init__(self, config: BaseConfigProvider, initialposition: Position,server_comm:ServerComm):
        BasicAntProducer.__init__(self, config)
        self.__server_comm = server_comm
        self.__AntsList = []
        self.__Counter = 0
        self.__InitialPosition = initialposition
        self.__max_num_of_ants = int(config.GetConfigValueForSectionAndKey('SimpleAnt', 'NumToProduce'))

    def CreateAnts(self):
        ids = self.__server_comm.GetAntsIds()

        for id in ids:

            startingPosition = Position(x=self.__InitialPosition.X, y=self.__InitialPosition.Y)
            ant = AlgoAnt(id, self._Config, startingPosition)
            self.__AntsList.append(ant)

    def added_ants(self, num_of_ants_produced, world_image):
        ants_to_add = []
        ids = self.__server_comm.GetAntsIds()
        startingPosition = Position(x=self.__InitialPosition.X, y=self.__InitialPosition.Y)
        for id in ids:
            if next((x for x in self.__AntsList if x.ID == int(id)), None) is None:
                ant = AlgoAnt(id, self._Config, startingPosition)
                ant.UpdatePosition(position=Position(x=self.__InitialPosition.X, y=self.__InitialPosition.Y))
                ants_to_add.append(ant)
                self.__AntsList.append(ant)
        return ants_to_add

    def _StopIteration(self) -> bool:
        if (self.__Counter >= len(self.__AntsList) - 1):
            return True
        return False

    def _NextAnt(self) -> AlgoAnt:

        if self._StopIteration():
            return self.__AntsList[self.__Counter - 1]

        ant = self.__AntsList[self.__Counter]
        self.__Counter += 1
        return ant

    def _CountAntType(self, Role: AntType):
        counter = 0
        for ant in self.__AntsList:
            if ant.GetRole() == Role:
                counter += 1
        return counter

    def __iter__(self):
        return self

    def __next__(self) -> AlgoAnt:
        if self._StopIteration():
            self.__Counter = 0
            raise StopIteration
        else:
            return self._NextAnt()
