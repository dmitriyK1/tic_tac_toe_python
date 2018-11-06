def render():
    print('\n')

    for row_index, row in enumerate(model):
        for index, column in enumerate(row):
            val = column if column else ' '

            print(f'{val}', end='')

            if index != 2:
                print('|', end='')
        if row_index != 2:
            print('\n-----')
