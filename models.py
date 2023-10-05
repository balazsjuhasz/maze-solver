from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)
