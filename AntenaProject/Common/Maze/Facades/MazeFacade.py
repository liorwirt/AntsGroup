import numpy as np
from AntenaProject.Common.Maze.Parsers.BaseMazeParser import BaseMazeParser
import networkx as nx
from AntenaProject.Common.AntsBasicStructures.Position import Position
from networkx.readwrite import json_graph

class MazeFacade(object):

    def __init__(self,mazeparser:BaseMazeParser):
        self.__MazeParser=mazeparser

        self.__GenrateGraph()
    def GetMatrix(self)->np.ndarray:
        return self.__MazeParser.GetMatrix()
    def GetEnterence(self):
        return self.__MazeParser.GetEnterence()
    def GetExits(self):
        return self.__MazeParser.GetExits()
    def GetDims(self):
        return self.__MazeParser.GetDims()
    def MayMove(self,src:Position,dst:Position,maxNumberOfSteps=1):
        if(src==dst):
            return True
        try:
            path=self.__GetPath(src,dst)
            #src and dst are returened
            lengthofpath=len(path)-2
            return (lengthofpath>=0 and lengthofpath<maxNumberOfSteps )
        except:
            return False
    def IsObs(self,position:Position)->bool:
        return  self.__MazeParser.IsObs(position)

    @property
    def ConnectivityGraph(self):
        return self.__Graph

    @property
    def Name(self):
        return self.__MazeParser.GetName()

    def __GetPath(self,src:Position,dst:Position):

        width, height = self.__MazeParser.GetDims()
        path = nx.shortest_path(self.__Graph, self.__ToGridNode(src.X,src.Y, height),
                                self.__ToGridNode(dst.X,dst.Y, height))
        realpath = []
        for cord in path:
            x = self.__Graph.nodes[cord]["X"]
            y = self.__Graph.nodes[cord]["Y"]
            realpath.append((y, x))
        return realpath
    def __ToGridNode(self,y,x, rownumber):
        return x + (y * rownumber)
    def __GenrateGraph(self):

        width, height = self.__MazeParser.GetDims()
        labels = {}
        self.__Graph = nx.Graph()
        for colIndex in range(0, width):
            for rowIndex in range(0, height):
                if (self.__MazeParser.GetMatrix()[rowIndex][colIndex] == 1):
                    coord = self.__ToGridNode(rowIndex, colIndex, height)
                    # we set connectivity
                    self.__Graph.add_node(coord)
                    self.__Graph.nodes[coord]["X"] = colIndex
                    self.__Graph.nodes[coord]["Y"] = rowIndex

        for node in self.__Graph.nodes:
            colIndex = self.__Graph.nodes[node]["X"]
            rowIndex = self.__Graph.nodes[node]["Y"]
            self.__UpdateWeight(node, colIndex, rowIndex, 0, 1)
            self.__UpdateWeight(node, colIndex, rowIndex, 0, -1)
            self.__UpdateWeight(node, colIndex, rowIndex, -1, 0)
            self.__UpdateWeight(node, colIndex, rowIndex, -1, 1)
            self.__UpdateWeight(node, colIndex, rowIndex, -1, -1)
            self.__UpdateWeight(node, colIndex, rowIndex, 1, 0)
            self.__UpdateWeight(node, colIndex, rowIndex, 1, -1)
            self.__UpdateWeight(node, colIndex, rowIndex, 1, 1)
    def __UpdateWeight(self, node, colIndex, rowIndex, xFactor, yFactor):
        width, height = width, height = self.__MazeParser.GetDims()
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
        vertexweight = 1
        if (self.__MazeParser.GetMatrix()[newRowIndex][newColIndex] == 1):
            # we try to go to Cover -not connected
            NextCord = self.__ToGridNode(newRowIndex, newColIndex, height)
            # we set connectivity
            self.__Graph.add_edge(NextCord, node, weight=vertexweight)
