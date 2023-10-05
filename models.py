from __future__ import annotations
from tkinter import Tk, Canvas


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
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._is_running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self._canvas, fill_color)


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = win

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(
                Line(
                    Point(self._x1, self._y1),
                    Point(self._x1, self._y2),
                ),
                "black",
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(
                    Point(self._x2, self._y1),
                    Point(self._x2, self._y2),
                ),
                "black",
            )
        if self.has_top_wall:
            self._win.draw_line(
                Line(
                    Point(self._x1, self._y1),
                    Point(self._x2, self._y1),
                ),
                "black",
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(
                    Point(self._x1, self._y2),
                    Point(self._x2, self._y2),
                ),
                "black",
            )

    def draw_move(self, to_cell: Cell, undo: bool = False):
        center_x = (self._x1 + self._x2) // 2
        center_y = (self._y1 + self._y2) // 2
        other_center_x = (to_cell._x1 + to_cell._x2) // 2
        other_center_y = (to_cell._y1 + to_cell._y2) // 2
        if undo:
            color = "gray"
        else:
            color = "red"

        self._win.draw_line(
            Line(
                Point(center_x, center_y),
                Point(other_center_x, other_center_y),
            ),
            color,
        )
