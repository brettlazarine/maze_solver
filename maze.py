from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None) -> None:
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    
    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                c = self._draw_cell(i, j)
                row.append(c)
            self._cells.append(row)
        

    def _draw_cell(self, i ,j):
        if self._win is None:
            return None
        
        cell = Cell(self._win)
        cell._x1 = self._x1 + i * self._cell_size_x
        cell._y1 = self._y1 + j * self._cell_size_y
        cell._x2 = cell._x1 + self._cell_size_x
        cell._y2 = cell._y1 + self._cell_size_y
        cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
        self._animate()
        return cell
    
    
    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(.05)