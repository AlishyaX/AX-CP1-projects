#Alishya Xavier, ProficiencyTest: Tic-Tac-Toe
import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
        
    # Horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f'Player {row[0]} is the winner horizontally!')
    
    #Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally! (/)")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally! (\\)")
        return True
        
    #vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
        
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!(|)")
            return True 
    return False
        

def game_board(game_map, player = 0, row = 0, column = 0, display = False):
    try:
        if game_map[row][column] != 0:
            print('This position is already filled. Choose another.')
            return game_map, False
        print('   0  1  2')
        if not display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    
    except IndexError as e:
        print("Make sure you put a row/column as 0, 1, 2.", e)
        return game_map, False
    
    except Exception as e:
        print('Something went wrong.', e)
        return game_map, False

play = True
players = [1, 2]
while play:
    
    game_size = int(input("What size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game = game_board(game, display =True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        
        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input('What row do you want to play? (0, 1, 2): '))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input('That game is over, would you like to play again? (y/n) ')
            if again.lower() == 'y':
                print('restarting')
            elif again.lower() == 'n':
                print('Thankyou for playing!')
                play = False
            else:
                print('That is not one of the options.')
                play = False


game = game_board(game, display = True)
game = game_board(game_board, player =1, row =2, column =1)
#game[0][1] = 1

