from Life import Life


def test_one():
    game = Life(3, 3)

    game.board = [[0, 0, 0],
                 [0, 1, 1],
                 [0, 1, 0]]

    game.do_next_move()

    assert game.board == [[0, 0, 0],
                          [0, 1, 1],
                          [0, 1, 1]]


test_one()
