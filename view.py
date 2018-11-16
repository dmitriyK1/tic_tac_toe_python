import os


def get_cell_view_value(model, row, cell):
    return model[row][cell] or ' '


def map_model_to_cell_values(model):
    cell_view_values = []

    for row_index, row in enumerate(model):
        for cell_index, cell in enumerate(row):
            cell_view_values.append(get_cell_view_value(model, row_index, cell_index))

    return cell_view_values


def get_view(model):
    cell_view_values = map_model_to_cell_values(model)

    return f'''
    {cell_view_values[0]}|{cell_view_values[1]}|{cell_view_values[2]}
    _____
    {cell_view_values[3]}|{cell_view_values[4]}|{cell_view_values[5]}
    _____
    {cell_view_values[6]}|{cell_view_values[7]}|{cell_view_values[8]}
    '''

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


def render(model):
    os.system('cls' if os.name == 'nt' else 'clear')

    view = get_view(model)

    print(view)
