def update():
    view()

    while True:
        for player in ('X', 'O'):
            if is_game_over():
                return

            do_next_turn(player)
