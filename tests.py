import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cell(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        self.assertEqual(len(m1._cells), num_cols)

    def test_maze_create_diff_cell(self):
        num_cols = 15
        num_rows = 17
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_diff_cells(self):
        num_cols = 15
        num_rows = 17
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=10)
        self.assertEqual(len(m1._cells), num_cols)
    

    def test_maze_break_entrance_and_exit(self):
        cols = 12
        rows = 10

        m = Maze(0, 0, rows, cols, 10, 10, seed=10)
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[cols - 1][rows - 1].has_bottom_wall, False)

    
    def test_maze_reset_cells(self):
        cols = 12
        rows = 10

        m = Maze(0, 0, rows, cols, 10, 10, seed=10)
        m._cells[0][0]._visited = True
        m._cells[-1][-1]._visited = True
        m._reset_cells()
        self.assertEqual(m._cells[0][0]._visited, False)
        self.assertEqual(m._cells[-1][-1]._visited, False)


if __name__ == "__main__":
    unittest.main()