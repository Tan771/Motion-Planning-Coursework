#!/usr/bin/env python3

from grid_planners import TetrisGridGenerator
import numpy as np 
from queue import Queue
import time
import matplotlib.pyplot as plt

class GridPlanners:
    """
    @brief Collection of Grid Bades Planners 
    """

    def __init__(self, grid) -> None:
        self.grid = grid
        self.four_neighbours = [[-1,0],
                                [1,0],
                                [0,1],
                                [0,-1]]
        self.eight_neighbours = [[-1,-1],
                                 [-1,0],
                                 [-1,1],
                                 [1,0],
                                 [0,1],
                                 [0,-1],
                                 [1,-1],
                                 [1,1]] 
    
    def get_path(self, start, goal, parent_node):
        path = []
        node = (goal[0],goal[1])

        while node != (start[0], start[1]):
            path.append(node)
            node = parent_node[node]
        path.append(start)

        return path[::-1]

    def set_endpoints_to_zero(self, start, goal):
        grid_copy = [row[:] for row in self.grid]
        grid_copy[start[0]][start[1]] = 0
        grid_copy[goal[0]][goal[1]] = 0

        return grid_copy

    def bfs_planner(self, start, goal, visualize=False):
        self.grid = self.set_endpoints_to_zero(start, goal)
        start_time = time.perf_counter()
        visited = set()
        node_queue = Queue()
        parent_node = {}
        found = False
        node_queue.put(start)
        visited.add((start[0],start[1]))
        
        while not node_queue.empty():
            node = node_queue.get()

            if node == goal:
                found = True
                break

            for neighbour in self.eight_neighbours:
                x_ = node[0] + neighbour[0]
                y_ = node[1] + neighbour[1]

                if 0 <= x_ < len(self.grid) and 0 <= y_ < len(self.grid[0]) and self.grid[x_][y_]!=1 and (x_, y_) not in visited:
                    node_queue.put([x_,y_])
                    visited.add((x_, y_))
                    parent_node[(x_,y_)] = (node[0], node[1])
        
        if found:
            path = self.get_path(start, goal, parent_node)
            print(f"Found path in {len(path)}  steps and took {time.perf_counter() - start_time} secs")
        else:
            print(f"Failed to find a path and took {time.perf_counter() - start_time} secs")
            path = []

        return path
    
    def dfs_path(self, start, goal, visualize=False):
        self.grid = self.set_endpoints_to_zero(start, goal)

        visited = set()
        node_queue = Queue()
        parent_node = {}
        found = False
        node_queue.put(start)
        visited.add((start[0],start[1]))
    
    def visualize_path(self, path):
        grid_with_path = np.array(self.grid)  # Create a copy of the grid for visualization
        for node in path:
            grid_with_path[node[0]][node[1]] = 2  # Mark path nodes with a different value
        # print(path)
        plt.imshow(grid_with_path, cmap="gray", interpolation='nearest')
        plt.xticks([])
        plt.yticks([])
        plt.show()

                
        
