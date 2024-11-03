from graphics import *

def main():
    win = Window(800, 600)

    point1 = Point(0, 0)
    point2 = Point(500, 500)

    line = Line(point1, point2)
    
    win.draw_line(line, "red")

    cell1 = Cell(win)
    cell1.draw(100, 500, 200, 200)
    cell2 = Cell(win)
    cell2.draw(200, 100, 300, 700)
    cell3 = Cell(win)
    cell3.draw(300, 100, 400, 200)
    cell4 = Cell(win)
    cell4.draw(400, 600, 500, 200)

    win.wait_for_close()

if __name__ == "__main__":
    main()