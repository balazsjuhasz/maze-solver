from tkinter import BOTH, Canvas, Tk


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(
            self._root,
            bg="white",
            width=width,
            height=height,
        )
        self._canvas.pack(fill=BOTH, expand=1)
        self._is_running = False

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self) -> None:
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self._canvas, fill_color)
