#Alishya Xavier, ProficiencyTest: Tic-Tac-Toe

game = [[1, 1, 1],
         [0, 2, 0],
         [2, 2, 0],]

for col in range(len(game)):


def win(current_game):
    # Horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f'Player {row[0]} is the winner horizontally!')
    
    #Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally!")

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally!")
        
        
        
        for row in game:
            check.append(row[col])
        if check.count9check[0]) 
        

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
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    
    game_won = False
    game = game_board(game, display =True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input('What row do you want to play? (0, 1, 2): '))
        game = game_board(game, current_player, row_choice, column_choice)




game = game_board(game, display = True)
game = game_board(game_board, player =1, row =2, column =1)
#game[0][1] = 1

