from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.MeshAnts.mesh_ant import mesh_ant
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.AntZTest.RobotCommuincation.ServerComm import ServerComm
from AntenaProject.MeshAnts.connectivty_calculator import connectivty_calculator
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade

class RobotMeshAntProducer(BasicAntProducer):

    def __init__(self,config:BaseConfigProvider,initialposition:Position,server_comm:ServerComm,maze:MazeFacade,connectivty_calculator:connectivty_calculator):
        BasicAntProducer.__init__(self,config)
        self.__server_comm=server_comm
        self.__AntsList = []
        self.__Counter = 0
        self.__InitialPosition=initialposition
        self.__connectivty_calculator = connectivty_calculator
        self.__maze = maze

    def CreateAnts(self):
        ids=self.__server_comm.GetAntsIds()

        for id in ids:
            ant=mesh_ant(str(id),self.__maze,self.__connectivty_calculator,self._Config)
            ant.UpdatePosition(position=Position(x=self.__InitialPosition.X,y=self.__InitialPosition.Y))

            self.__AntsList.append(ant)


    def _StopIteration(self) -> bool:
        if(self.__Counter>=len(self.__AntsList)-1):

            return True
        return False

    def _NextAnt(self) -> mesh_ant:

        if self._StopIteration():
            return self.__AntsList[ self.__Counter-1]

        ant= self.__AntsList[self.__Counter]
        self.__Counter += 1
        return ant
    def __iter__(self):
        return self

    def __next__(self) -> mesh_ant:
        if self._StopIteration():
            self.__Counter = 0
            raise StopIteration
        else:
            return self._NextAnt()

    def added_ants(self, num_of_ants_produced, world_image):
        ants_to_add = []
        ids = self.__server_comm.GetAntsIds()

        for id in ids:
            if next((x for x in self.__AntsList if x.ID == int(id)), None) is None:
                ant = mesh_ant(id,self.__maze,self.__connectivty_calculator,self._Config)
                ant.UpdatePosition(position=Position(x=self.__InitialPosition.X, y=self.__InitialPosition.Y))
                ants_to_add.append(ant)
                self.__AntsList.append(ant)
        return ants_to_add