#import sudoku as s


def is_valid(sudoku, row, col, guess):
    # Chack on the rows
    #for i in sudoku:
    row_check = sudoku[row]
    if guess in row_check:
        return False
    # Check on the columns
    aux = []
    for i in range(9):
        aux.append(sudoku[i][col])
    if guess in aux:
        return False

    # Check the squers
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if sudoku[r][c] == guess:#guess in colu:
                return False

    return True


def find_empty_space(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None, None


def solver(sudoku):
    if not sudoku:
        exit()

    row, col = find_empty_space(sudoku)

    if row is None:
        return True

    for guess in range(1,10):
        if is_valid(sudoku, row, col, guess):
            sudoku[row][col] = guess

            if solver(sudoku):
                return True

        sudoku[row][col] =  0

    return False

#if __name__ == '__main__':
#    sudoku = [
#        [0,1,0,6,0,7,0,0,4],
#        [0,4,2,0,0,0,0,0,0],
#        [8,7,0,3,0,0,6,0,0],
#        [0,8,0,0,7,0,0,2,0],
#        [0,0,0,8,9,3,0,0,0],
#        [0,3,0,0,6,0,0,1,0],
#        [0,0,8,0,0,6,0,4,5],
#        [0,0,0,0,0,0,1,7,0],
#        [4,0,0,9,0,8,0,6,0],
#    ]
#    for i in sudoku:
#        print(i)
#    print(solver(sudoku))
#    for i in sudoku:
#        print(i)
#    
