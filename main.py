import random


def main():
    grid = createGrid(3)
    randomizeGrid(grid)
    print(grid)


def createGrid(size):
    grid = [[0 for i in range(size)] for j in range(size)]
    counter = 0
    for i in range(size):
        for j in range(size):
            grid[i][j] = counter
            counter += 1

    return grid


def randomizeGrid(grid):
    random.shuffle(grid)


def printGrid(grid):
    for i in range(grid.size()):
        print(grid[i] + "\n")


main()
