#Gameboard
#0 : {1: NA, 2 3 4 5}
#1 : {1:x, 2:x, 3:x, 4:x, 5:x}
#2 : {1:x, 2:x, 3:x, 4:x, 5:x}
#......

import random

class Gameboard:
    #create a board
    def __init__(self, num_row, num_column):
        self.num_row = num_row
        self.num_column = num_column
        self.board = [["X" for j in range(num_column)] for i in range(num_row)]
       
        self.ship_row = random.randrange(0, num_row)
        self.ship_column = random.randrange(0, num_column)

    # def __setitem__():

    #Grid with dictionaries if you ever want to do this never
        # for row in range(1,self.num_row+1):
        #     self.board.update({str(row): {}})
        #     for column in range(1,self.num_column+1):
        #         self.board[str(row)].update({str(column): "X"})



        



