from graphics import *

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.draw(10, 10, 100, 100)
    cell2 = Cell(win)
    cell2.draw(500, 500, 600, 600)
    cell1.draw_move(cell2)

    win.wait_for_close()

if __name__ == "__main__":
    main()