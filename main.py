from drawing import Window
from maze import Maze

if __name__ == "__main__":
    width = 800
    height = 600
    num_rows = 10
    num_cols = 10
    margin = 25
    cell_size_x = (width - 2 * margin) // num_cols
    cell_size_y = (height - 2 * margin) // num_rows

    win = Window(width, height)
    maze = Maze(
        margin,
        margin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    )
    maze.solve()

    win.wait_for_close()
