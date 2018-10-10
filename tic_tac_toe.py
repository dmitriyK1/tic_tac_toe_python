model = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def view():
    for row in model:
        for column in row:
            print(f'{column}|', end='')
        print()


#
# def view():
#     s = f'''\
# {model[0][0]}|{model[0][1]}|{model[0][2]}
# _____
# {model[1][0]}|{model[1][1]}|{model[1][2]}
# _____
# {model[2][0]}|{model[2][1]}|{model[2][2]}
#     '''
#
#     print(s)
#
#
def get_player_input():
    row = int(input('select row(1-3):')) - 1
    cell = int(input('select cell(1-3):')) - 1

    if row > 2 or cell > 2:
        return get_player_input()
    else:
        return row, cell


def update():
    view()

    while True:
        row, cell = get_player_input()
        model[row][cell] = 'X'
        view()

        row, cell = get_player_input()
        model[row][cell] = 'O'
        view()

        print(f'row:{row} cell:{cell}')


update()
