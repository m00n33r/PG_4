import pygame

from Board import Board


def main():
    pygame.init()
    cube_length = 50
    frm = 10
    n = (10, 15)
    size = [cube_length * n[0] + 2 * frm, cube_length * n[1] + 2 * frm]
    screen = pygame.display.set_mode(size)

    running = True
    board = Board(*n, cube_length, frm)

    clock = pygame.time.Clock()
    while running:

        screen.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        board.render(screen)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()


if __name__ == '__main__':
    main()
