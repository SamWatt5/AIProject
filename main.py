import random


def main():
    grid = createGrid(3)
    randomizeGrid(grid)
    printGrid(grid)
    turn(grid, 1, 1)


def createGrid(size):
    grid = [[0 for i in range(size)] for j in range(size)]
    counter = 0
    for i in range(size):
        for j in range(size):
            if counter == 0:
                grid[i][j] = " "
            else:
                grid[i][j] = counter
            counter += 1

    return grid


def randomizeGrid(grid):
    gridContents = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            gridContents.append(grid[i][j])
    random.shuffle(gridContents)
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = gridContents[counter]
            counter += 1


def printGrid(grid):
    for row in grid:
        print(" ".join(f"{tile}" for tile in row))

    print("")


def check(grid, x, y):
    print("checked grid[" + str(x) + "][" + str(y) + "] = " + str(grid[x][y]))
    if grid[y][x] == " ":
        return True
    return False


def turn(grid, x, y):
    # up x y-1
    if check(grid, x, y-1):
        print("up")
    # down x y+1
    elif check(grid, x, y+1):
        print("down")
    # left x-1 y
    elif check(grid, x-1, y):
        # do something
        print("left")
    # right x+1 y
    elif check(grid, x+1, y):
        print("right")
        # do something
    else:
        print("cant move")


main()
