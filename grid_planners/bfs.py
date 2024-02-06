from grid_planners.grid_planners_interface import GridBasedPlanners

import time 
from queue import Queue

class BFS(GridBasedPlanners):
    def plan(self, start, goal):
        start,goal = self.set_endpoints_to_Node(start, goal)
        start_time = time.perf_counter()
        visited = set()
        node_queue = Queue()
        found = False
        node_queue.put(start)
        visited.add((start.x,start.y))
        
        while not node_queue.empty():
            node = node_queue.get()

            if node == goal:
                goal = node
                found = True
                break

            for neighbour in self.eight_neighbours:
                x_ = node.x + neighbour[0]
                y_ = node.y + neighbour[1]

                if 0 <= x_ < len(self.grid) and 0 <= y_ < len(self.grid[0]) and self.grid[x_][y_]!=1 and (x_, y_) not in visited:
                    node_queue.put(self.Node(x_,y_,0,0,node))

                    visited.add((x_, y_))
        if found:
            path = self.get_path(start, goal)
            print(f"Found path in {len(path)}  steps and took {time.perf_counter() - start_time} secs")
        else:
            print(f"Failed to find a path and took {time.perf_counter() - start_time} secs")
            path = []

        return path