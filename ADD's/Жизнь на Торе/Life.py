from copy import deepcopy
from Board import Board


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def on_click(self, cell_coords):
        if not cell_coords: return
        x, y = cell_coords
        self.board[y][x] = int(not self.board[y][x])

    def do_next_move(self):
        copy_board = deepcopy(self.board)
        new_board = [[0] * self.width for _ in range(self.height)]
        for i in range(len(copy_board[0])):
            for j in range(len(copy_board)):
                new_board[j][i] = self.get_val(i, j)
        self.board = new_board

    def get_val(self, i, j):
        cnt = 0
        cell = self.board[j][i]
        for x in range(j - 1, j + 2):
            for y in range(i - 1, i + 2):
                if (x, y) == (j, i):
                    continue
                if self.board[x % self.height][y % self.width] == 1:
                    cnt += 1
        ans = 0

        if cell == 0 and cnt == 3:
            ans = 1
        elif cell == 1 and cnt in (2, 3):
            ans = 1

        return ans

    def test(self, arr):
        self.board = arr
