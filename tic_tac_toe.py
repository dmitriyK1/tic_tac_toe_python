model = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def view():
    for row in model:
        for column in row:
            val = column if column else ' '

            print(f'{val}|', end='')
        print()


def get_player_input():
    row = int(input('select row(1-3):')) - 1
    cell = int(input('select cell(1-3):')) - 1

    if row > 2 or cell > 2:
        print('value out of range')
        return get_player_input()

    return row, cell


def update():
    view()

    while True:
        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'X'
        view()

        row, cell = get_player_input()

        while model[row][cell]:
            print('cell already occupied')
            row, cell = get_player_input()

        model[row][cell] = 'O'
        view()

        print(f'row:{row} cell:{cell}')


update()
