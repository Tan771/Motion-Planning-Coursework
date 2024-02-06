import numpy as np 
import random
import matplotlib.pyplot as plt 


class TetrisGridGenerator:
    """
    @brief Class for generating and visualizing Tetris-like grids.
    """
    
    def __init__(self, rows=480, cols=720):
        """
        @brief Initialize TetrisGridGenerator with specified number of rows and columns.

        @param rows: Number of rows in the grid.
        @param cols: Number of columns in the grid.
        """
        self.rows = rows
        self.cols = cols 
        self.grid = []
    
    def get_grid(self, packing_percentage=50):
        """
        @brief Generate a Tetris-like grid with the given packing percentage.

        @param packing_percentage: Occupancy percentage for the Tetris-like grid.

        @return: Generated Tetris-like grid.
        """
        if not (0 <= packing_percentage <= 100):
            raise ValueError("Packing percentage should be between 0 and 100.")

        total_cells = self.rows * self.cols 
        occupied_cells = int(total_cells * packing_percentage /100)
        self.grid = np.zeros((self.rows,self.cols))

        for _ in range(occupied_cells):
            while True:
                x = random.randint(0, self.rows-1)
                y = random.randint(0, self.cols-1)

                if self.grid[x][y] == 0:
                    self.grid[x][y] = 1
                    break
        

        return self.grid

    def plot_grid(self, grid):
        """
        @brief Display the provided grid using Matplotlib.

        @param grid: The grid to be displayed.
        """
        plt.imshow(grid, cmap='Blues', interpolation='nearest')
        plt.xticks([])
        plt.yticks([])
        plt.show()


def main():
    tetris_generator = TetrisGridGenerator(100,100)
    grid1 = tetris_generator.get_grid(10)
    grid2 = tetris_generator.get_grid(25)
    grid3 = tetris_generator.get_grid(50)

    tetris_generator.plot_grid(grid1)
    tetris_generator.plot_grid(grid2)
    tetris_generator.plot_grid(grid3)


if __name__ == "__main__":
    main()