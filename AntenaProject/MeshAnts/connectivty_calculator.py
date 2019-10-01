from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt, Position
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from typing import List
import networkx as nx
class connectivty_calculator():
    def __init__(self,config,maze_facade:MazeFacade):
        self.__conncetivity_radius=(int)(config.GetConfigValueForSectionAndKey("SimpleAnt","connectivity_range"))
        self.__maze_facade=maze_facade

    def does_move_affect_connectivity(self,next_position:Position,ant_id,world_image)->bool:

        if(len(world_image.Ants())<2):
            return False
        currnet_graph=nx.Graph()
        ants=world_image.Ants()
        for outer_ant in ants:
            currnet_graph.add_node(outer_ant)
            for inner_ant in ants:
                if(inner_ant==outer_ant):
                    continue
                if self.__is_los(ants[outer_ant],ants[inner_ant]):
                    currnet_graph.add_edge(outer_ant,inner_ant)
        #test against new position
        for outer_ant in ants:
            if(ant_id== outer_ant):
                continue
            if self.__is_los( ants[outer_ant],next_position):
                currnet_graph.add_edge(outer_ant, ant_id)
            else:
                if(currnet_graph.has_edge(outer_ant, ant_id)):
                    currnet_graph.remove_edge(outer_ant, ant_id)
        is_connected=nx.is_connected(currnet_graph)
        return not is_connected






    def __is_los(self,pFrom: Position, pTo: Position)->bool:
        if(pTo==pFrom):
            return True
        los_points=self._bres(pFrom,pTo)
        if len(los_points)==0:
            return False
        if len(los_points)>self.__conncetivity_radius:
            return False

        for position in los_points:
            if self.__maze_facade.IsObs(position=position):
                return False

        return True
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






