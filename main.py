from models import Window, Point, Cell

if __name__ == "__main__":
    win = Window(800, 600)
    cell2 = Cell(Point(200, 100), Point(300, 200), win)
    cell2.has_right_wall = False
    cell2.draw()

    cell4 = Cell(Point(300, 100), Point(400, 200), win)
    cell4.has_left_wall = False
    cell4.draw()

    cell2.draw_move(cell4)

    win.wait_for_close()
