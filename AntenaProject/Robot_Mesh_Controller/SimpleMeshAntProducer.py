from AntenaProject.Common.AntsBasicStructures.BasicAntProducer import BasicAntProducer
from AntenaProject.MeshAnts.mesh_ant import mesh_ant
from AntenaProject.Common.Config.BaseConfigProvider import BaseConfigProvider
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.AntZTest.RobotCommuincation.ServerComm import ServerComm
from AntenaProject.MeshAnts.connectivty_calculator import connectivty_calculator
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade

class SimpleMeshAntProducer(BasicAntProducer):

    def __init__(self,config:BaseConfigProvider,initialposition:Position,maze:MazeFacade,connectivty_calculator:connectivty_calculator,number_to_produce):
        BasicAntProducer.__init__(self,config)
        self.__AntsList = []
        self.__Counter = 0
        self.__InitialPosition=initialposition
        self.__connectivty_calculator = connectivty_calculator
        self.__maze = maze
        self.__number_to_produce=number_to_produce
        self.__new_ID=0

    def CreateAnts(self):
        ids=range(self.__number_to_produce)

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

        if(len(self.__AntsList)==self.__number_to_produce):
            return ants_to_add

        for ant in self.__AntsList:
            if(ant.CurrentPosition==self.__InitialPosition):
                return ants_to_add
        ant = mesh_ant(self.__new_ID, self.__maze, self.__connectivty_calculator, self._Config)
        ant.UpdatePosition(position=Position(x=self.__InitialPosition.X, y=self.__InitialPosition.Y))
        ants_to_add.append(ant)
        self.__AntsList.append(ant)

        self.__new_ID+=1
        return ants_to_add
