from window import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line, "white")


    def draw_move(self, to_cell, undo=False):
        half = abs(self.x2 - self.x1) // 2
        x_center = half + self.x1
        y_center = half + self.y1

        half2 = abs(to_cell.x2 - to_cell.x1) // 2
        x_center2 = half2 + to_cell.x1
        y_center2 = half2 + to_cell.y1

        fill_color = "red"
        if undo:
            fill_color = "grey"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.win.draw_line(line, fill_color)

