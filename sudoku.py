"""
To play SUDOKU.
"""
import solver


def greeting():
    """Presentation.
    """
    print("""
                 WELCOME TO SUDOKU
                      columns 
                       v v v
                 0 1 2|3 4 5|6 7 8
                ,-----------------,
               0|     |     |     |
               1|     |     |     |
               2|     |     |     |
               -|-----------------|
            >  3|     |     |     |
     rows   >  4|     |     |     |
            >  5|     |     |     |
               -|-----------------|
               6|     |     |     |
               7|     |     |     |
               8|     |     |     |
                `-----------------'
          """)
    input("Enter to continue.")


def get_field(field):
    try:
        while True:
            try:
                value = input(f"{field}: ")
                if value.isdigit():
                    value = int(value)
                    if value > 9:
                        raise ValueError
                    return value
            except ValueError:
                print(f"{value} is not valid ")
                continue
    except KeyboardInterrupt:
        print("Bye, Bye!!")
        exit()


def logic(sudoku):
    if not sudoku:
        exit()

    row = get_field('row')
    col = get_field('column')
    if row >= 9 or col >= 9:
        print(f"Invalid row: {row} or/and column: {col}.")
        return
    number = get_field('number')

    if solver.is_valid(sudoku, row, col, number):
        sudoku[row][col] = number
        if win(sudoku):
            return True
    else:
        print('Invalid Move \n Try again.')


def display_board(grid):
    """Print de board on the screen.
    """

    line = "-"*25
    for x in range(9):
        if x%3 == 0:
            print(line)
        row = ""
        for y in range(9):
            if y%3 == 0:
                row += "| "
            value = str(grid[x][y]) if grid[x][y] > 0 else " "
            row += value + " "
        row += "|"
        print(row)
    print(line)


def win(sudoku):
    """looking for a winner.
    it will Check all over the board.
    rows, cols and grids variables once are all True the GAME is OVER.
    """
    rows = False
    cols = False
    grids = False

    if not rows:            # it will Check the rows
        for i in sudoku:
            i = set(i)      # castting the list i to set(it doesn't allow repeated Values)
            if len(i) == 9: # once is True it means there's valid and not repeated Values
                rows = True
            else:
                rows = False
                break

    if not cols:
        for i in range(9):
            aux = []                  # Auxiliar to store the values
            for j in range(9):
                aux.append(sudoku[j][i])
            aux = set(aux)
            if len(aux) == 9:
                cols = True
            else:
                cols = False
                break


    if not grids:
        for row in range(9):
            for col in range(9):
                row_start = (row // 3) * 3# Values where begins the rows iteration
                col_start = (col // 3) * 3# Values where begins the columns iteration
                aux = []                  # Auxiliar to store the values
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        aux.append(sudoku[i][j])
                aux = set(aux)
                if len(aux) == 9:
                    grids = True
                else:
                    grids = False
                    break

    if rows and cols and grids:
        return True
    else:
        return False


def game(sudoku):
    while True:
        display_board(sudoku)
        board = logic(sudoku)

        if board == True:
            print("It's done")
            print("GAME OVER")
            break
