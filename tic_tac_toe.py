# TODO: use https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.matrix.html
model = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def view():
    for rowIndex, row in enumerate(model):
        for index, column in enumerate(row):
            val = column if column else ' '

            print(f'{val}', end='')

            if index != 2:
                print('|', end='')
        if rowIndex != 2:
            print('\n-----')


def get_player_input():
    row = int(input('select row(1-3):')) - 1
    cell = int(input('select cell(1-3):')) - 1

    if row > 2 or cell > 2:
        print('value out of range')
        return get_player_input()

    return row, cell


def check_is_game_over():
    for row in model:
        if None in row:
            return False

    print('GAME OVER.')
    return True


def update():
    view()

    while True:
        if check_is_game_over():
            break

        # TODO: refactor into a helper function
        print('\n')
        print('First player turn')
        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'X'
        view()

        if check_is_game_over():
            break

        print('\n')
        print('Second player turn')
        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'O'
        view()


update()
