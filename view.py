import os


def get_view(model):
    return f'''
    {model[0][0] or ' '}|{model[0][1] or ' '}|{model[0][2] or ' '}
    _____
    {model[1][0] or ' '}|{model[1][1] or ' '}|{model[1][2] or ' '}
    _____
    {model[2][0] or ' '}|{model[2][1] or ' '}|{model[2][2] or ' '}
    '''


def render(model):
    os.system('cls' if os.name == 'nt' else 'clear')

    view = get_view(model)

    print(view)

    # for row_index, row in enumerate(model):
    #     for index, column in enumerate(row):
    #         val = column if column else ' '
    #
    #         print(f'{val}', end='')
    #
    #         if index != 2:
    #             print('|', end='')
    #     if row_index != 2:
    #         print('\n-----')
