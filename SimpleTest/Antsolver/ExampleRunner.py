from map_class import Map
from ant_colony import AntColony
from MazeGraphSolver import MazeGraphSolver
from SolutionDrawing import SolutionDrawing
from MapFileLoader import MapFileLoader
import time
import numpy as np
import sys
import argparse


if __name__ == '__main__':
    ants=100
    iterations=1
    p=0.5
    Q=2
    map_path="map3.txt"
    mapfileloader=MapFileLoader(map_path)
    # Get the map
    Map= Map(mapfileloader)
    Colony = AntColony(Map, ants, iterations, p, Q)

    graph=MazeGraphSolver(mapfileloader)
    starttime=time.time()
    acopath = Colony.calculate_path()
    print(format(f"it took ACO {time.time()-starttime} sec to find a path"))
    starttime = time.time()
    print(acopath)

    optimalpath=graph.GetPath()
    print(format(f"it took Optimal graph find {time.time() - starttime} sec to find a path"))

    SD=SolutionDrawing(Map.initial_node,Map.final_node,Map.occupancy_map)
    SD.DrawPaths(acopath,optimalpath)