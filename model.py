MODEL = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


# TODO maybe return a new model instance from here (without mutating it)
# def set_model(prev_model, row, cell, value):
def set_model(row, cell, value):
    MODEL[row][cell] = value


def get_model():
    return MODEL
