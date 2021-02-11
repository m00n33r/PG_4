import pygame

from Life import Life


def main():
    pygame.init()
    cube_length = 25
    frm = 10
    n = (30, 20)
    size = [cube_length * n[0] + 2 * frm, cube_length * n[1] + 2 * frm]
    screen = pygame.display.set_mode(size)

    game = Life(*n)
    game.set_view(frm, frm, cube_length)
    running = True
    living = 0

    clock = pygame.time.Clock()
    while running:

        screen.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not living:
                    game.get_click(event.pos)
            if event.type == pygame.TEXTINPUT:
                living = (living + 1) % 2

        if living:
            game.do_next_move()

        game.render(screen)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()


if __name__ == '__main__':
    main()
