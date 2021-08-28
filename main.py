import sudoku
import solver# as ss
import puzzle


if __name__ == '__main__':
    puzzle = puzzle.get_board()
    sudoku.greeting()

    try:
        print("\n")
        choice = input("Play or autosolve(p/a): ")

        if choice == 'p':
            sudoku.game(puzzle)
        elif choice == 'a':
            try:
                sudoku.display_board(puzzle)
                print('Working...')
                solver.solver(puzzle)
                sudoku.display_board(puzzle)
            except ImportError:
                print("File doesnt import")
        else:
            print("Invalid option.")
    except:
        pass

