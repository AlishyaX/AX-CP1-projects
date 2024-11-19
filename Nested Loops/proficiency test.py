#Alishya Xavier, TicTacToe project

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def print_board():
    for row in board:
        print('|'.join(row))
        print('-----')

def check_win(player):
    #This checks each of the rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    #This checks each of the columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    #This checks each of the diagnols
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][i-2] == player for i in range(3)):
        return True


