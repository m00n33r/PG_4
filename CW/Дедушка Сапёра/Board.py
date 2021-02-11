import pygame
from random import randint

pygame.font.init()


class Board:
    def __init__(self, width, height, tile, frm):
        self.width = width
        self.height = height

        self.map = [[[-1, False]for _ in range(width)] for _ in range(height)]
        self.set_map()

        self.left, self.top = frm, frm
        self.tile = tile

    def set_map(self):
        for i in range(self.height):
            self.map[i][randint(0, self.width - 1)][0] = 10

    def get_cell_value(self, i, j):
        cell_num = 0
        for s, x in enumerate(range(max(0, j - 1), min(self.height, j + 2))):
            for h, y in enumerate(range(max(0, i - 1), min(self.width, i + 2))):
                if self.map[x][y][0] == 10:
                    cell_num += 1
        return cell_num

    def render(self, screen):
        mx_left = self.width * self.tile + self.left
        mx_top = self.height * self.tile + self.top
        for x, i in enumerate((range(self.left, mx_left, self.tile))):
            for y, j in enumerate(range(self.top, mx_top, self.tile)):
                pygame.draw.rect(screen, pygame.Color('dimgray'),
                                 (i, j, self.tile, self.tile), 1)
                self.draw_item(screen, (x, y), (i, j))
                if self.map[y][x][1]:
                    self.open_cell(screen, (x, y), (i, j))

    def open_cell(self, screen, id_, coords):
        myfont = pygame.font.Font(pygame.font.get_default_font(), 30)
        text_num = myfont.render(str(self.get_cell_value(*id_)), True, (0, 255, 0))
        screen.blit(text_num, coords)

    def draw_item(self, screen, id_, coords):
        i, j = coords
        x, y = id_
        pygame.draw.rect(screen, pygame.Color('black'),
                         (i + 1, j + 1, self.tile - 2, self.tile - 2))
        if self.map[y][x][0] == 10:
            pygame.draw.rect(screen, pygame.Color('red'),
                             (i + 1, j + 1, self.tile - 2, self.tile - 2))
        if self.map[y][x][1]:
            self.open_cell(screen, id_, coords)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        ans = None
        i, j = mouse_pos
        x, y = (i - self.left) // self.tile, (j - self.top) // self.tile
        if 0 <= x < len(self.map[0]) and 0 <= y < len(self.map):
            ans = (x, y)
        return ans

    def on_click(self, cell_coords):
        if not cell_coords or self.map[cell_coords[1]][cell_coords[0]][0] == 10:
            return
        self.map[cell_coords[1]][cell_coords[0]][1] = True
