import os


# TODO
def get_view_template(model): pass


def render(model):
    os.system('cls' if os.name == 'nt' else 'clear')

    for row_index, row in enumerate(model):
        for index, column in enumerate(row):
            val = column if column else ' '

            print(f'{val}', end='')

            if index != 2:
                print('|', end='')
        if row_index != 2:
            print('\n-----')
