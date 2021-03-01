import pygame

from Lines import Lines


def main():
    pygame.init()
    cube_length = 25
    frm = 10
    n = (30, 20)
    size = [cube_length * n[0] + 2 * frm, cube_length * n[1] + 2 * frm]
    screen = pygame.display.set_mode(size)

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
                    if game.has_path(*cords1, *cords2, n):
                        game.board[cords2[1]][cords2[0]] = 1
                        game.board[cords1[1]][cords1[0]] = -1
                else:
                    game.get_click(event.pos)

        game.render(screen)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()


if __name__ == '__main__':
    main()
