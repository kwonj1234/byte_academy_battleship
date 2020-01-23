#initalize and create a new board
def main_menu():
    rows = input("How many rows for battleship?\n")
    columns = input("How many columns for battleship?\n")
    return rows, columns

#print board
def show_board(board, rows):
    board_view = []
    for row in range(rows):
        board_view.append(" | ".join(board[row]))
        print(board_view[row])

#input a guess
def input_coordinates():
    print("Input firing coordinates")

def guess_x():
    guess_column = input("\nTarget X-Coordinate\n")
    return guess_column

def guess_y():
    guess_row = input("\nTarget Y-Coordinate\n")
    return guess_row

#fire
def fire():
    print("\nFIRE!!!\n")

#miss message
def miss():
    print("\nYou've missed")
#win message
def win():
    print("\nCongratulations, you sunk the enemy battleship")

#Bad input
def not_num():
    print("\nInput a number\n")

def input_not_in_range(numrow_or_numcolumn):
    print(f"\nInput a number between 1 and {numrow_or_numcolumn}")
