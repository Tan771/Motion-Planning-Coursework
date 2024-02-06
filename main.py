from environment.tetris_grid_generator import TetrisGridGenerator
from grid_planners.bfs import BFS
from grid_planners.dfs import DFS

def main():
    grid_handle = TetrisGridGenerator(100,100)
    grid = grid_handle.get_grid(20)
    print(grid.shape)
    bfs_planner = BFS(grid)

    bfs_path = bfs_planner.plan([0, len(grid[0])-1], [len(grid)-1,0])
    bfs_planner.visualize_path(bfs_path)

    dfs_planner = DFS(grid)

    dfs_path = dfs_planner.plan([0, len(grid[0])-1], [len(grid)-1,0])
    dfs_planner.visualize_path(bfs_path)


main()