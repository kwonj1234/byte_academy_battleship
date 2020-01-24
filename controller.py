import model
import view

def run():
    play = True
    while play == True:
        rows, columns = view.main_menu()
        #return error for non-numeric input
        if rows.isnumeric() == False or columns.isnumeric() == False:
            view.not_num()
        play = False

    rows = int(rows)
    columns = int(columns)
    battleship = model.Gameboard(rows, columns)
    view.show_board(battleship.board, rows)
    print(battleship.ship_row, battleship.ship_column)
    print(type(battleship.board))

    play = True
    while play == True:
        #TODO Error handling when input is out of range or not number
        view.input_coordinates()
        #return error for non-numeric input or not in range input
        guess_again = True
        while guess_again == True:
            guess_column = view.guess_x()
            if guess_column.isnumeric() == False:
                view.not_num()
            elif int(guess_column) > columns or int(guess_column) < 1:
                view.input_not_in_range(columns)
            else:
                guess_again = False

        guess_again = True
        while guess_again == True:
            guess_row = view.guess_y()
            if guess_row.isnumeric() == False:
                view.not_num()
            elif int(guess_row) > rows or int(guess_row) < 1:
                view.input_not_in_range(rows)
            else:
                guess_again = False

        guess_row = int(guess_row)-1
        guess_column = int(guess_column)-1
        view.fire()
            
        #Compare guess to battleship location
        #win condition
        if guess_row == battleship.ship_row and guess_column == battleship.ship_column:
            battleship.board[guess_row][guess_column] = "S"
            view.win()
            view.show_board(battleship.board, rows)
            return 
        #miss condition
        battleship.board[guess_row][guess_column] = "X"
        view.miss()
        view.show_board(battleship.board, rows)

run()
