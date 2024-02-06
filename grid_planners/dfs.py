from grid_planners_interface import GridBasedPlanners

class DFS(GridBasedPlanners):
    def __init__(self, grid_map) -> None:
        super().__init__(grid_map)
    
    def plan(self, start, goal):
        return None