from AntenaProject.Common.AntsBasicStructures.BasicAnt import BasicAnt, Position
from AntenaProject.Common.Maze.Facades.MazeFacade import MazeFacade
from copy import deepcopy
from typing import List,Dict
import networkx as nx
class path_builder():
    def __init__(self,config,maze_facade:MazeFacade):
        self.__maze_facade=maze_facade

    def __build_connectivity_matrix(self,maze_facade:MazeFacade):
        self.__path_graph=nx.Graph()
        maze_width,maze_height=maze_facade.GetDims()
        for x in range(maze_width):
            for y in range(maze_height):
                node=self.__coord_to_node(x,y)
                self.__path_graph.add_node(node)

        for x in range(maze_width):
            for y in range(maze_height):
                node = self.__coord_to_node(x, y)
                left_node_x=x-1
                right_node_x = x + 1
                top_node_y=y-1
                bottom_node_y=y+1
                connected_nodes=[]
                connected_nodes.append(Position(x=x,y=top_node_y))
                connected_nodes.append(Position(x=x, y=bottom_node_y))
                connected_nodes.append(Position(x=left_node_x, y=y))
                connected_nodes.append(Position(x=right_node_x, y=y))
                for connected_node in connected_nodes:
                    if(maze_facade.is_in_bounds(connected_node)):
                        self.__path_graph.add_edge(node,self.__position_to_node(connected_node))

    def __clear_obs_nodes(self,obs_nodes:List[Position]):
        for obs_node in obs_nodes:
            node=self.__position_to_node(obs_node)
            if(node in self.__path_graph.nodes):
                self.__path_graph.remove_node(node)
    def get_paths_to_nodes(self,current_position:Position,exceluded_nodes:List[Position]=[])->Dict[Position,List[Position]]:

        self.__build_connectivity_matrix(self.__maze_facade)
        self.__clear_obs_nodes(exceluded_nodes)
        paths = nx.single_source_shortest_path( self.__path_graph,self.__position_to_node(current_position))
        path_resutltes={}
        for key,value in paths.items():
            path_resutlts_key=self.__node_to_position(key)
            path_result=[]
            for path_landmark in value:
                path_result.append(self.__node_to_position(path_landmark))
            path_resutltes[path_resutlts_key]=path_result

        return path_resutltes
    def __coord_to_node(self,x,y):
        return format(f'{x}_{y}')
    def __position_to_node(self,pos:Position):
        return self.__coord_to_node(pos.X,pos.Y)
    def __node_to_coord(self,node):
        return node.split('_')
    def __node_to_position(self,node)->Position:
        x,y=self.__node_to_coord(node)
        int_x=(int)(x)
        int_y=(int)(y)
        return Position(x=int_x,y=int_y)
