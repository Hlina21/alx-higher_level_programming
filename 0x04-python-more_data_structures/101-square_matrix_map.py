!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda submat: list(map(lambda a: a**2, submat)), matrix))
