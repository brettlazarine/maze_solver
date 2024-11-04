from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return 
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))

    def draw_move(self, to_cell, undo=False):
        line_color = "red" if not undo else "gray"

        self_half = abs(self._x1 - self._x2) // 2
        self_x_center = self_half + self._x1
        self_y_center = self_half + self._y1

        to_half = abs(to_cell._x1 - to_cell._x2) // 2
        to_x_center = to_half + to_cell._x1
        to_y_center = to_half + to_cell._y1

        self._win.draw_line(Line(Point(self_x_center, self_y_center), Point(to_x_center, to_y_center)), line_color)