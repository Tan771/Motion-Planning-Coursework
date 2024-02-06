from grid_planners.grid_planners_interface import GridBasedPlanners
import time 

class DFS(GridBasedPlanners):
    def __init__(self, grid_map) -> None:
        super().__init__(grid_map)
    
    def plan(self, start, goal):
        start, goal = self.set_endpoints_to_Node(start,goal)
        start_time = time.perf_counter()
        node_stack = [start]
        visited_set = set()
        vis_list = []
        found = False

        while len(node_stack):
            node = node_stack.pop()
            vis_list.append([node.x,node.y])
            if node == goal:
                goal = node
                found = True
                break

            for neighbour in self.four_neighbours:
                x_ = node.x + neighbour[0]
                y_ = node.y + neighbour[1]

                if 0<= x_ < len(self.grid) and 0 <= y_ < len(self.grid[0]) and self.grid[x_][y_]!=1 and (x_,y_) not in visited_set:
                    node_stack.append(self.Node(x_,y_,0,0,node))
                    visited_set.add((x_,y_))
            
        if found:
            path = self.get_path(start,goal)
            print(f"Found path in {len(path)} steps and in {time.perf_counter()-start_time} secs")
        else:
            path = []
            print(f"Failed to find a path")

        return path, list(vis_list)
