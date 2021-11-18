""" Matrix 90 degree rotation code """

def rotate_90(original):
    matrix = original[:]
    matrix = [k[::-1] for k in zip(*matrix)]
    return matrix


""" Matrix 180 degree rotation code """

def rotate_180(original):
    matrix = original[:]
    for i in range(2):
        matrix = [k[::-1] for k in zip(*matrix)]
    return matrix


""" Matrix 270 degree rotation code """

def rotate_270(original):
    matrix = original[:]
    for i in range(3):
        matrix = [k[::-1] for k in zip(*matrix)]
    return matrix


if __name__ == "__main__":
    m = [[i * j for i in range(5)] for j in range(5)]
    print(m)
    print(rotate_90(m))
    print(rotate_180(m))
    print(rotate_270(m))
