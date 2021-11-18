""" matrix transpose """

def transpose(original):
    matrix = original[:]
    matrix = [list(x) for x in zip(*matrix)]
    return matrix

