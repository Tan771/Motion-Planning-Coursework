from environment.tetris_grid_generator import TetrisGridGenerator
from grid_planners.bfs import BFS
from grid_planners.dfs import DFS
from utils.plot_animation import Plotting

def main():
    grid_handle = TetrisGridGenerator(100,100)
    grid, obs = grid_handle.get_grid(10)
    bfs_planner = BFS(grid)

    start = [0, 0]
    goal = [len(grid)-1,len(grid[0])-1]

    bfs_path, bfs_visited = bfs_planner.plan([0, len(grid[0])-1], [len(grid)-1,0])
    # bfs_planner.visualize_path(bfs_path)

    dfs_planner = DFS(grid)

    dfs_path, dfs_visited = dfs_planner.plan(start, goal)

    plot = Plotting(start, goal, obs)
    # plot.update_obs(grid)

    plot.animation(dfs_path, dfs_visited, "dfs path")
    # dfs_planner.visualize_path(dfs_path)

    plot.animation(bfs_path, bfs_visited, "bfs path")


main()