"""
Board generator
"""
from dokusan import generators


def get_board():
    arr = str(generators.random_sudoku(avg_rank=150))
    arr = [int(x) for x in arr]
    aux = []
    aux2 = []
    c = 0
    while c < len(arr):
        c += 1
        aux.append(arr[c-1])
        if c%9 == 0:
            aux2.append(aux)
            aux = []

    return aux2

