import tkinter as tk
import game


def main():
    window = tk.Tk()
    window.title("8-Puzzle Solver")

    grid = game.createGrid(3)

    game.shuffle(grid, 1000)
    game.printGrid(grid)

    target = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]

    buttons = {}
    for i in range(len(grid)):
        for j in range(len(grid)):
            button = tk.Button(
                text=grid[i][j],
                width=10,
                height=5,
                command=lambda x=j, y=i: button_click(grid, buttons, x, y, target))
            button.grid(row=i, column=j, padx=5, pady=5)
            buttons[(i, j)] = button

    window.mainloop()


def button_click(grid, buttons, x, y, target):
    game.turn(grid, x, y)
    update_buttons(grid, buttons)
    game.printGrid(grid)
    if game.check_solved(grid, target):
        print("SOLVED! :D")


def update_buttons(grid, buttons):
    for (i, j), button in buttons.items():
        button.config(text=grid[i][j])


if __name__ == "__main__":
    main()
