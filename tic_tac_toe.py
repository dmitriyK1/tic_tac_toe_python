# TODO: use https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.matrix.html
model = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def view():
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


def find_filled_columns():
    for index, row in enumerate(model):
        column_values = [row[index] for row in model]
        # print(column_values)

        if all(value == 'X' for value in column_values):
            print('\nplayer one won')
            return True
        elif all(value == 'O' for value in column_values):
            print('\nplayer two won')
            return True


def find_filled_rows():
    for row in model:
        # no need to check all row values if there's still empty slot
        if None in row:
            return False

        if all(cell_value == 'X' for cell_value in row):
            print('\n\nPlayer one won')
            return True
        elif all(cell_value == 'O' for cell_value in row):
            print('\n\nPlayer two won')
            return True

    return False


def find_filled_axis():
    pass


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
        print('\nFirst player turn')
        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'X'
        view()

        if check_is_game_over():
            break

        print('\nSecond player turn')
        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'O'
        view()


update()
