from copy import deepcopy

from .Board import *


class Game(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def on_click(self, cell_coords):
        if not cell_coords:
            return
        x, y = cell_coords
        self.board[y][x] = int(not self.board[y][x])

    def draw_item(self, screen, id, cord):
        i, j = cord
        x, y = id
        step = self.board[y][x]
        color = (0, 0, 0)
        if step == 1:
            color = (0, 255, 0)
            pygame.draw.rect(screen, color,
                             (i + 1, j + 1, self.cell_size - 2, self.cell_size - 2))
        else:
            pygame.draw.rect(screen, color,
                             (i + 1, j + 1, self.cell_size - 2, self.cell_size - 2))

    def next_move(self):
        copy_board = deepcopy(self.board)

        self.new_board = [[0] * self.width for _ in range(self.height)]
        for i in range(len(copy_board[0])):
            for j in range(len(copy_board)):
                self.new_board[j][i] = self.get_cell_value(i, j)
        self.board = self.new_board

    def get_cell_value(self, i, j):
        cell_n = 0
        cell = self.board[j][i]
        for s, x in enumerate(range(max(0, j - 1), min(self.height, j + 2))):
            for h, y in enumerate(range(max(0, i - 1), min(self.width, i + 2))):
                if (x, y) == (j, i):
                    continue
                if self.board[x][y] == 1:
                    cell_n += 1
        ans = 0
        if cell == 0 and cell_n == 3:
            ans = 1
        elif cell == 1 and cell_n in (2, 3):
            ans = 1
        return ans

    def create_gliders(self):
        if self.width >= 36 and self.height >= 9:
            pass
