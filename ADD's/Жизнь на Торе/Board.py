import pygame


class Board:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.board = [[0] * width for _ in range(height)]

        self.left, self.top = 10, 10
        self.tile = 10

    def set_view(self, left, top, tile):
        self.left = left
        self.top = top
        self.tile = tile

    def render(self, screen):
        mx_left = self.width * self.tile + self.left
        mx_top = self.height * self.tile + self.top
        for x, i in enumerate((range(self.left, mx_left, self.tile))):
            for y, j in enumerate(range(self.top, mx_top, self.tile)):
                pygame.draw.rect(screen, pygame.Color('dimgray'),
                                 (i, j, self.tile, self.tile), 1)
                self.draw_item(screen, (x, y), (i, j))

    def draw_item(self, screen, id_, coords):
        i, j = coords
        x, y = id_
        colors = (pygame.Color('black'), pygame.Color('green'))
        step = self.board[y][x]
        pygame.draw.rect(screen,
                         colors[step],
                         (i + 1, j + 1, self.tile - 2, self.tile - 2))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        ans = None
        i, j = mouse_pos
        x, y = (i - self.left) // self.tile, (j - self.top) // self.tile
        if 0 <= x < len(self.board[0]) and 0 <= y < len(self.board):
            ans = (x, y)
        return ans

    def on_click(self, cell_coords):
        if not cell_coords:
            return
