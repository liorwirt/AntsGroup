

from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt
from AntenaProject.Common.AntsBasicStructures.Position import Position
from AntenaProject.Common.AntsBasicStructures.Enums import NodeStateEnum
from AntenaProject.MeshAnts.connectivty_calculator import connectivty_calculator
from AntenaProject.Common.AntsBasicStructures.BaseSingleAntWorldImage import BaseSingleAntWorldImage
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from AntenaProject.MeshAnts.path_builder import path_builder
import random
from typing import  List
import numpy as np

class mesh_ant(BasicAnt):
    def __init__(self, id: int,maze:MazeFacade,connectivty_calculator:connectivty_calculator ,config):
        BasicAnt.__init__(self, id, config)
        self.__movement_range = (int)(config.GetConfigValueForSectionAndKey("SimpleAnt", "AllowedMovement"))
        self.__connectivty_calculator=connectivty_calculator
        self.__maze=maze
        self.__old_choice=[]
        self.__path_builder=path_builder(config,maze)
        self.__explored_map=np.ones(maze.GetDims())
        self.__last_steps=[]
        self.__last_steps_depth=2


    def _internalGetStep(self, antworldstate: BaseSingleAntWorldImage):
        path_resutltes=self.__path_builder.get_paths_to_nodes(self.CurrentPosition,self.__get_obs_on_path_grpah(antworldstate))
        for result in path_resutltes:
            #return first path we get-grreedy
            if not self.__was_node_explored(antworldstate,result):
                if self.CurrentPosition==result:
                    continue
                #first tep is origin
                next_step=path_resutltes[result][1]
                if not  self.__connectivty_calculator.does_move_affect_connectivity(next_position=next_step,ant_id=self._ID,world_image=antworldstate) \
                        and not self.__is_step_in_last_steps(next_step):
                    self.__update_last_steps(next_step)
                    print(format(f"for ant {self._ID} node {result} is was not explored so go to it with step {next_step}"))
                    return next_step, {}
                else:
                    print(format(f"for ant {self._ID} node {result} - step {next_step} breaks connectivity "))

            print(format(f"for ant {self._ID} node {result} is already explored so leave it at that!!!!"))
        return self.CurrentPosition, {}
    def __is_step_in_last_steps(self,next_step:Position)->bool:
        for step in self.__last_steps:
            if next_step==step:
                return True
        return False
    def __update_last_steps(self,next_step:Position):
        if len(self.__last_steps)==self.__last_steps_depth:
            self.__last_steps.pop(0)
        self.__last_steps.append(next_step)
    def __get_obs_on_path_grpah(self, antworldstate: BaseSingleAntWorldImage)->List[Position]:
        obstacels = []
        for node in antworldstate.VisibleNodes:
            if node.NodeState == NodeStateEnum.Obs:
                obstacels.append(node.Position)
        ants_to_positions=antworldstate.Ants()
        for ant_id in ants_to_positions:
            if ant_id!=self._ID:
                obstacels.append(ants_to_positions[ant_id])
        return obstacels
    def __was_node_explored(self, antworldstate: BaseSingleAntWorldImage, target_position: Position) -> bool:
        for node in antworldstate.WorldImage:
            # we have it so return if we need to ignore it
            if node.Position == target_position:
                return node.NodeState != NodeStateEnum.UnExplored
        return False
        # #update explored map
        # for node in antworldstate.WorldImage:
        #     self.__explored_map[node.Position.Y][node.Position.X]=0
        # #build pool
        # options = []
        # step=1
        # options.append(Position(x=self.CurrentPosition.X+step,y=self.CurrentPosition.Y))
        # options.append(Position(x=self.CurrentPosition.X-step,y=self.CurrentPosition.Y))
        # options.append(Position(x=self.CurrentPosition.X , y=self.CurrentPosition.Y+step))
        # options.append(Position(x=self.CurrentPosition.X , y=self.CurrentPosition.Y-step))
        #
        #
        #
        # positions=[]
        # for option in options:
        #     if not self.__maze.is_in_bounds(option):
        #         continue
        #     if not self.__maze.IsObs(option) and not self.__connectivty_calculator.does_move_affect_connectivity(option,self.ID,antworldstate):
        #         repatations =self.__get_repetitions_of_positions(antworldstate, option)
        #         for repatation in range(repatations):
        #             positions.append(option)
        #
        #
        #
        # if len (positions)==0:
        #     return self.CurrentPosition,{}
        #
        # new_position=random.choice(positions)
        # self.__old_choice.append(new_position)


    # def is_move_in_right_direction(self,current_position:Position,target_position:Position):


    # def __get_repetitions_of_positions(self,antworldstate: BaseSingleAntWorldImage,target_position:Position)->int:
    #     if target_position in self.__old_choice:
    #         return 0
    #     for node in antworldstate.VisibleNodes:
    #         if node.Position == target_position:
    #             return 0
    #         if node.NodeState == NodeStateEnum.Obs:
    #             return 0
    #         if node.NodeState == NodeStateEnum.Ant:
    #             return 0
    #         if node.NodeState == NodeStateEnum.Clear:
    #             return 1
    #         if node.NodeState == NodeStateEnum.UnExplored:
    #             return 20
    #
