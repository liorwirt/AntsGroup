#!/usr/bin/env python
from MapFileLoader import MapFileLoader
import numpy as np
import matplotlib.pyplot as plt

class Map:
    ''' Class used for handling the
        information provided by the
        input map '''
    class Nodes:
        ''' Class for representing the nodes
            used by the ACO algorithm '''
        def __init__(self, row, col, in_map,spec):
            self.node_pos= (row, col)
            self.edges = self.compute_edges(in_map)
            self.spec = spec

        def compute_edges(self,map_arr):
            ''' class that returns the edges
                connected to each node '''
            imax = map_arr.shape[0]
            jmax = map_arr.shape[1]
            edges = []
            if map_arr[self.node_pos[0]][self.node_pos[1]] == 1:
                for dj in [-1,0,1]:
                    for di in [-1,0,1]:
                        newi = self.node_pos[0]+ di
                        newj = self.node_pos[1]+ dj
                        if ( dj == 0 and di == 0):
                            continue
                        if (newj>=0 and newj<jmax and newi >=0 and newi<imax):
                            if map_arr[newi][newj] == 1:
                                edges.append({'FinalNode':(newi,newj),
                                              'Pheromone': 1.0, 'Probability':
                                             0.0})
            return edges

    def __init__(self, mapfileloader):
        self.in_map = mapfileloader.in_map
        self.occupancy_map = mapfileloader.occupancy_map
        self.initial_node = mapfileloader.initial_node
        self.final_node= mapfileloader.final_node
        self.nodes_array = self._create_nodes()

    def _create_nodes(self):
        ''' Create nodes out of the initial map '''
        return [[self.Nodes(i,j,self.occupancy_map,self.in_map[i][j]) for j in
                 range(self.in_map.shape[0])] for i in range(self.in_map.shape[0])]




