from utils import is_game_over, do_next_turn
from view import render


def update(model):
    render(model)

    while True:

        for player in ('X', 'O'):
            if is_game_over(model):
                return

            do_next_turn(model, player)
            render(model)
