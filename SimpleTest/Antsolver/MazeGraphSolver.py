
import os
import networkx as nx
from networkx.readwrite import json_graph
import json
import  io
import itertools
import numpy as np


class MazeGraphSolver(object):
    def __init__(self,mapfileloader):

        self.__in_map = mapfileloader.in_map
        self.__occupancy_map = mapfileloader.occupancy_map
        self.initial_node = mapfileloader.initial_node
        self.final_node = mapfileloader.final_node


        self.__BuildGraph()

    def GetGraph(self):
        return self._Graph



    def __getMapDim(self):
        return  self.__occupancy_map.shape
    def GetPath(self):
        width, height = self.__getMapDim()
        path = nx.shortest_path(self._Graph, self.__ToGridNode(self.initial_node[0],self.initial_node[1],height), self.__ToGridNode(self.final_node[0],self.final_node[1],height))
        realpath=[]
        for cord in path:
            x=self._Graph.nodes[cord]["X"]
            y=self._Graph.nodes[cord]["Y"]
            realpath.append((y,x))
        return realpath

    def __ToGridNode(self,x,y,rownumber):
        return x + (y * rownumber)
    def __BuildGraph(self):
        width,height = self.__getMapDim()
        labels = {}
        self._Graph = nx.Graph()
        for colIndex in range(0, width):
            for rowIndex in range(0, height):
                if (self.__occupancy_map[rowIndex][colIndex] == 1):
                    coord = self.__ToGridNode(colIndex, rowIndex, height)
                    # we set connectivity
                    self._Graph.add_node(coord)
                    self._Graph.nodes[coord]["X"] = colIndex
                    self._Graph.nodes[coord]["Y"] = rowIndex

        for node in self._Graph.nodes:
            colIndex=self._Graph.nodes[node]["X"]
            rowIndex=self._Graph.nodes[node]["Y"]
            self._UpdateWeight(node, colIndex, rowIndex, 0, 1)
            self._UpdateWeight(node, colIndex, rowIndex, 0, -1)
            self._UpdateWeight(node, colIndex, rowIndex, -1, 0)
            self._UpdateWeight(node, colIndex, rowIndex, -1, 1)
            self._UpdateWeight(node, colIndex, rowIndex, -1, -1)
            self._UpdateWeight(node, colIndex, rowIndex, 1, 0)
            self._UpdateWeight(node, colIndex, rowIndex, 1, -1)
            self._UpdateWeight(node, colIndex, rowIndex, 1, 1)



    def _UpdateWeight(self, node, colIndex, rowIndex, xFactor, yFactor):
        width, height= self.__getMapDim()
        newColIndex = colIndex + xFactor
        newRowIndex = rowIndex + yFactor
        if (newColIndex) >= width:
            return
        if (newColIndex) < 0:
            return
        if (newRowIndex) >= height:
            return
        if (newRowIndex) < 0:
            return
        vertexweight=1
        if(self.__occupancy_map[newRowIndex][newColIndex]==1):
            # we try to go to Cover -not connected
            NextCord = self.__ToGridNode(newColIndex, newRowIndex, height)
            # we set connectivity
            self._Graph.add_edge(NextCord, node, weight=vertexweight)
