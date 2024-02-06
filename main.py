from environment.tetris_grid_generator import TetrisGridGenerator
from grid_planners.bfs import BFS

def main():
    grid_handle = TetrisGridGenerator(100,100)
    grid = grid_handle.get_grid(20)

    bfs_planner = BFS(grid)

    bfs_path = bfs_planner.plan([0, len(grid[0])-1], [len(grid)-1,0])
    bfs_planner.visualize_path(bfs_path)


main()