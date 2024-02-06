#!/usr/bing/env python3
import time 
import numpy as np
import matplotlib.pyplot as plt

class GridBasedPlanners:
    """
    @brief Interface class for all the grid based planners
    """
    def __init__(self, grid_map) -> None:
        self.grid = grid_map
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

    class Node:
        def __init__(self,x,y,is_obs=0,cost=0,parent=None) -> None:
            self.x = x
            self.y = y
            self.is_obs = is_obs
            self.cost = cost
            self.parent = parent
        
        def __eq__(self, other):
            return isinstance(other, self.__class__) and (self.x, self.y) == (other.x, other.y)

        def __repr__(self):
            return f"Node(x={self.x}, y={self.y}, is_obs={self.is_obs}, cost={self.cost}, parent={self.parent})"
        
    def get_path(self, start, goal):
        path = []
        node = goal
        while node != None:
            path.append([node.x,node.y])
            node = node.parent

        return path
    
    def visualize_path(self, path):
        grid_with_path = np.array(self.grid)  # Create a copy of the grid for visualization
        for node in path:
            grid_with_path[node[0]][node[1]] = 2  # Mark path nodes with a different value
        # print(path)
        plt.imshow(grid_with_path, cmap="Blues", interpolation='nearest')
        plt.xticks([])
        plt.yticks([])
        plt.show()

    
    def set_endpoints_to_Node(self, start, goal):
        start = self.Node(start[0],start[1])
        goal = self.Node(goal[0],goal[1])

        return start, goal

    def plan(self, start, goal):
        return ValueError("Planner not implemented")
    
