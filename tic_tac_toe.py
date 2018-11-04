# TODO: use https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.matrix.html
model = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def view():
    print('\n')

    for row_index, row in enumerate(model):
        for index, column in enumerate(row):
            val = column if column else ' '

            print(f'{val}', end='')

            if index != 2:
                print('|', end='')
        if row_index != 2:
            print('\n-----')


def get_player_input():
    row = int(input('select row(1-3):')) - 1
    cell = int(input('select cell(1-3):')) - 1

    if row > 2 or cell > 2:
        print('value out of range')
        return get_player_input()

    return row, cell


def has_player_one_won(values):
    if all(value == 'X' for value in values):
        return True


def has_player_two_won(values):
    if all(value == 'O' for value in values):
        return True


def has_some_player_won(values):
    if has_player_one_won(values):
        print('\n\nplayer one won')
        return True

    if has_player_two_won(values):
        print('\n\nplayer two won')
        return True


def find_filled_columns():
    for index in range(len(model)):
        column_values = [row[index] for row in model]

        if has_some_player_won(column_values):
            return True


def find_filled_rows():
    for row in model:
        # no need to check all row values if there's still empty slot
        if None in row:
            return False

        if has_some_player_won(row):
            return True


def is_axis_filled(axis_values, mark):
    return all(axis_value == mark for axis_value in axis_values)


def find_filled_axis():
    axis_values = [row[index] for (index, row) in enumerate(model)]
    reverse_axis_values = [row[len(model) - index - 1] for (index, row) in enumerate(model)]

    if has_some_player_won(axis_values) or has_some_player_won(reverse_axis_values):
        return True


def check_is_game_over():
    if find_filled_rows() or find_filled_columns() or find_filled_axis():
        print('\nGAME OVER.')
        return True

    return False


def update():
    view()

    while True:
        if check_is_game_over():
            break

        # TODO: refactor into a helper function
        print('\n\nFirst player turn')
        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'X'
        view()

        if check_is_game_over():
            break

        print('\n\nSecond player turn')
        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'O'
        view()


update()
