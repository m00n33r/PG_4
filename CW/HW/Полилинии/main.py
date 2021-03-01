import pygame

from Lines import Lines


def main():
    pygame.init()
    cube_length = 40
    frm = 10
    n = (10, 6)
    size = [cube_length * n[0] + 2 * frm, cube_length * n[1] + 2 * frm]
    screen = pygame.display.set_mode(size)
    z, i = 0, -1

    game = Lines(*n)
    game.set_view(frm, frm, cube_length)
    running = True

    clock = pygame.time.Clock()
    while running:

        screen.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.check_red() is not None and game.get_color(game.get_cell(event.pos)) == -1:
                    cords2 = game.get_cell(event.pos)
                    cords1 = game.check_red()
                    z = game.has_path(*cords1, *cords2, n)
                    if z != 0:
                        i = len(z) - 2
                else:
                    game.get_click(event.pos)

        if z != 0:
            game.board[z[i + 1][1]][z[i + 1][0]] = -1
            game.board[z[i][1]][z[i][0]] = 1
            i -= 1
            if i == -1:
                z = 0

        game.render(screen)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()


if __name__ == '__main__':
    main()
