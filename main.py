from models import Window, Line, Point

if __name__ == "__main__":
    win = Window(800, 600)
    line1 = Line(Point(400, 300), Point(0, 0))
    line2 = Line(Point(400, 300), Point(800, 0))
    line3 = Line(Point(400, 300), Point(800, 600))
    line4 = Line(Point(400, 300), Point(0, 600))
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.draw_line(line3, "green")
    win.draw_line(line4, "blue")
    win.wait_for_close()
