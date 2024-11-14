#Alishya Xavier, ProficiencyTest: Tic-Tac-Toe

game = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]

def game_board(game_map, player = 0, row = 0, column = 0, display = False):
    print('   0  1  2')
    if not display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

game = game_board(game, display = True)
game = game_board(game, player =1, row =2, column =1)
#game[0][1] = 1

