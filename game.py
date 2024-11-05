import random


def main():
    grid = createGrid(3)
    randomizeGrid(grid)
    printGrid(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            turn(grid, j, i)


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


def shuffle(grid, numShuffles):
    for i in range(numShuffles):
        turn(grid, random.randint(0, len(grid)-1),
             random.randint(0, len(grid)-1))


def printGrid(grid):
    for row in grid:
        print(" ".join(f"{tile}" for tile in row))

    print("")


def check(grid, x, y):
    # print("checked grid[" + str(x) + "][" + str(y) + "] = " + str(grid[x][y]))

    if x > len(grid)-1 or y > len(grid)-1 or x < 0 or y < 0:
        return False
    if grid[y][x] == " ":
        return True
    return False


def turn(grid, x, y):
    # print(grid[y][x])

    # up x y-1
    if check(grid, x, y-1):
        grid[y][x], grid[y-1][x] = grid[y-1][x], grid[y][x]
        # printGrid(grid)
    # down x y+1
    elif check(grid, x, y+1):
        grid[y][x], grid[y+1][x] = grid[y+1][x], grid[y][x]
        # printGrid(grid)
    # left x-1 y
    elif check(grid, x-1, y):
        # do something
        grid[y][x], grid[y][x-1] = grid[y][x-1], grid[y][x]
        # printGrid(grid)
    # right x+1 y
    elif check(grid, x+1, y):
        grid[y][x], grid[y][x+1] = grid[y][x+1], grid[y][x]
        # printGrid(grid)
        # do something
    # else:
        # print("cant move")


def check_solved(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != target[i][j]:
                return False
    return True
