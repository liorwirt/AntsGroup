from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt, Position
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from typing import List

import networkx as nx
import numpy as np
class connectivty_calculator():
    def __init__(self,config,maze_facade:MazeFacade):
        self.__conncetivity_radius=(int)(config.GetConfigValueForSectionAndKey("SimpleAnt","connectivity_range"))
        self.__maze_facade=maze_facade
        self.__enterence_position=maze_facade.GetEnterence()
        self.__enterence_key=1000

    def does_move_affect_connectivity(self,next_position:Position,ant_id,world_image)->bool:

        if(len(world_image.Ants())<2):
            return False
        currnet_graph=nx.Graph()

         #add enterence
        ants=world_image.Ants()
        ants[ self.__enterence_key]= self.__enterence_position
        for outer_ant in ants:
            currnet_graph.add_node(outer_ant)
            for inner_ant in ants:
                if(inner_ant==outer_ant):
                    continue
                los_points=self._los_calcuation_function(ants[outer_ant],ants[inner_ant])
                if self.__is_los_according_to_constraiants(ants[outer_ant],ants[inner_ant],los_points):
                    currnet_graph.add_edge(outer_ant,inner_ant)

        #test against new position
        for outer_ant in ants:
            if(ant_id== outer_ant):
                continue
            los_points = self._los_calcuation_function(ants[outer_ant],next_position)
            if self.__is_los_according_to_constraiants( ants[outer_ant],next_position,los_points):
                currnet_graph.add_edge(outer_ant, ant_id)
            else:
                if(currnet_graph.has_edge(outer_ant, ant_id)):
                    currnet_graph.remove_edge(outer_ant, ant_id)
        is_connected=nx.is_connected(currnet_graph)
        return not is_connected






    def __is_los_according_to_constraiants(self,pFrom: Position, pTo: Position,los_points:List[Position])->bool:
        if(pTo==pFrom):
            return True

        if len(los_points)==0:
            return False
        if len(los_points)>self.__conncetivity_radius:
            return False

        for position in los_points:
            if self.__maze_facade.IsObs(position=position):
                return False

        return True

    def _los_calcuation_function(self,pFrom: Position, pTo: Position)->List[Position]:
        return self._bres(pFrom,pTo)

    def _bres(self, pFrom: Position, pTo: Position)->List[Position]:
        end = False
        x0 = pFrom.X
        y0 = pFrom.Y
        x1 = pTo.X
        y1 = pTo.Y
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        if x0 < x1:
            sx = 1
        else:
            sx = -1

        if y0 < y1:
            sy = 1
        else:
            sy = -1
        err = dx - dy
        LOSpoints = []
        while not end:
            if x0 == x1 and y0 == y1:
                end = True
                LOSpoints.append(Position(x1, y1))
                return LOSpoints
            e2 = 2 * err
            if e2 > -dy:
                err = err - dy
                x0 = x0 + sx
            if e2 < dx:
                err = err + dx
                y0 = y0 + sy
            LOSpoints.append(Position(x0, y0))
        return LOSpoints

    def get_connectivity_lines(self,ants_positons):
        connectivity_lines=[]
        ants_positons[self.__enterence_key] = self.__enterence_position
        for outer_key in ants_positons:
            for inner_key in ants_positons:
                if(inner_key==outer_key):
                    continue
                index_to_remove=[]
                los_points = self._los_calcuation_function(ants_positons[inner_key], ants_positons[outer_key])


                if self.__is_los_according_to_constraiants(ants_positons[inner_key], ants_positons[outer_key], los_points):
                    filtered_los_points = filter(lambda x: x != ants_positons[outer_key] and x != ants_positons[inner_key],
                                      los_points)

                    connectivity_lines.append(list(filtered_los_points))

        return connectivity_lines






