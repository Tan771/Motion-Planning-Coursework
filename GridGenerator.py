import numpy as np 
import random
import matplotlib.pyplot as plt 

class TetrisGridGenerator:
    def __init__(self, rows=480, cols=720):
        self.rows = rows
        self.cols = cols 
        self.grid = []
    
    def get_grid(self, packing_percentage=50):
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
        plt.imshow(grid, cmap='Blues', interpolation='nearest')
        plt.xticks([])
        plt.yticks([])
        plt.show()


def main():
    tetris_generator = TetrisGridGenerator(100,100)
    grid1 = tetris_generator.get_grid(10)
    grid2 = tetris_generator.get_grid(50)
    grid3 = tetris_generator.get_grid(75)

    tetris_generator.plot_grid(grid1)
    tetris_generator.plot_grid(grid2)
    tetris_generator.plot_grid(grid3)


if __name__ == "__main__":
    main()