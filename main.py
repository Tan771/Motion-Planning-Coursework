from GridGenerator import TetrisGridGenerator
from GridPlannes import GridPlanners

def main():
    grid_handle = TetrisGridGenerator(1000,1000)
    grid = grid_handle.get_grid(30)

    planner = GridPlanners(grid)

    bfs_path = planner.bfs_planner([0, len(grid[0])-1], [len(grid)-1,0])
    planner.visualize_path(bfs_path)


main()