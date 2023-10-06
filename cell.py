from __future__ import annotations
from typing import Optional

from drawing import Line, Point, Window


class Cell:
    def __init__(
        self,
        top_left: Point,
        bottom_right: Point,
        win: Optional[Window] = None,
    ):
        self.visited: bool = False
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = win

    def draw(self):
        if self._win is None:
            return

        # Left wall
        self._win.draw_line(
            Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2),
            ),
            "black" if self.has_left_wall else "white",
        )

        # Right wall
        self._win.draw_line(
            Line(
                Point(self._x2, self._y1),
                Point(self._x2, self._y2),
            ),
            "black" if self.has_right_wall else "white",
        )

        # Top wall
        self._win.draw_line(
            Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1),
            ),
            "black" if self.has_top_wall else "white",
        )

        # Bottom wall
        self._win.draw_line(
            Line(
                Point(self._x1, self._y2),
                Point(self._x2, self._y2),
            ),
            "black" if self.has_bottom_wall else "white",
        )

    def draw_move(self, to_cell: Cell, undo: bool = False):
        if self._win is None:
            return

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
