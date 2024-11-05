from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None) -> None:
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells()

    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        

    def _draw_cell(self, i ,j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    
    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(.01)

    
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw(entrance_cell._x1, entrance_cell._y1, entrance_cell._x2, entrance_cell._y2)
        
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw(exit_cell._x1, exit_cell._y1, exit_cell._x2, exit_cell._y2)

    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            lst = []

            if i > 0 and not self._cells[i - 1][j]._visited:
                lst.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1]._visited:
                lst.append((i, j - 1))
            if i < self._num_cols - 1 and not self._cells[i + 1][j]._visited:
                lst.append((i + 1, j))
            if j < self._num_rows - 1 and not self._cells[i][j + 1]._visited:
                lst.append((i, j + 1))

            if not lst:
                self._draw_cell(i, j)
                return
            
            random_index = random.randrange(len(lst))
            random_cell = lst[random_index]

            if random_cell[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            elif random_cell[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            elif random_cell[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            elif random_cell[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            
            self._draw_cell(i, j)
            self._break_walls_r(random_cell[0], random_cell[1])

    
    def _reset_cells(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False