game_list = [['_','_','_'],['_','_','_'],['_','_','_']]
sample_list = ['_','_','_']

def display_gamelist(game_list):
    for i in range(len(game_list)):
        for j in range(len(game_list[i])):
            print(game_list[i][j], end = ' ')
        print()
#display the userinput board
def inital_display():
    print("Welcome to TicTacToe PVP")
    print('First the user must pick their choice of x or o')
    print("You will first be asked to pick a row num (0-2)")
    print("Then you'll have to pick a colum num (0-2)")
    print('Here are the positions you can refrence')
    print(['0 0','0 1','0 2'])
    print(['1 0','1 1','1 2'])
    print(['2 0','2 1','2 2'])

def position_display():
        print('Here are the positions you can refrence')
        print(['0 0','0 1','0 2'])
        print(['1 0','1 1','1 2'])
        print(['2 0','2 1','2 2'])

def game_win(game_list):
    #check horizontal
    if (game_list[0][0] == game_list [0][1] == game_list [0][2] and game_list[0][0] != '_' ) or (game_list[1][0] == game_list [1][1] == game_list [1][2]  and game_list[1][1] != '_' ) or (game_list[2][0] == game_list [2][1] == game_list [2][2] and game_list[2][2] != '_'):
        return True
        print('Game Won')
    else:
        return False
    #check vertical
    if (game_list[0][0] == game_list [1][0] == game_list [2][0]) or (game_list[0][1] == game_list [1][1] == game_list [2][1]) or (game_list[0][2] == game_list [1][2] == game_list [2][2]):
        return True
        print('Game Won')
    else:
        return False
    #check diagnol
    if (game_list[0][0] == game_list [1][1] == game_list [2][2]) or (game_list[0][2] == game_list [1][1] == game_list [2][0]):
        return True
        print('Game Won')
    else:
        return False


def get_row():
    choice = 'Incorrect'
    while choice not in ['0','1','2']:
        choice = input("Please pick which row you would play your turn in [0, 1, 2] ")
        if choice not in ['0','1','2']:
            print("Invalid choice, please enter only the numbers from [0,1,2] ")
    return int(choice)

def get_col():
    choice = 'Incorrect'
    while choice not in ['0','1','2']:
        choice = input('You have chosen the row, please pick the col you would like to play in [0, 1, 2] ')
        if choice not in ['0','1','2']:
            print("Please only enter numbers from [0,1,2] ")
    return int(choice)

def position_replace():
    print('Please chose what to play either x or o: ')
    choice = 'incorrect'
    while choice not in ['x', 'X', 'o', 'O']:
        choice = input ('Enter either x or o ')
        if choice not in ['x', 'X', 'o', 'O']:
            print('Please pick either o or x')
    return choice

def replace_game(game_list, row, col, choice):
    game_list[row][col] = choice
    return game_list

#this function will take the row and col and check if the given position has already been filled
def precheck_position(game_list, row, col, choice, moves_list):
    if game_list[row][col] != '_' or moves_list[-1] == choice:
        return False
    else:
        return True

def draw(game_list):
    for i in range(len(game_list)):
        for j in range(len(game_list[i])):
            if game_list[i][j] != '_':
                return True
            else:
                 return False

#get the inital move from the player
inital_display()
moves_list = []
choice = position_replace()
row = get_row()
col = get_col()
game_list = replace_game(game_list,row,col,choice)
moves_list.append(choice)
display_gamelist(game_list)

game_draw = False
game_fini = False
while game_fini == False:
    position_display()
    choice = position_replace()
    row = get_row()
    col = get_col()
    pre_check = precheck_position(game_list, row, col, choice, moves_list)
    if pre_check == True:
        game_list = replace_game(game_list,row,col,choice)
        moves_list.append(choice)
    else:
        print("You can not over ride a position")
        print("You can not play the same character twice in a row")
    display_gamelist(game_list)
    game_fini = game_win(game_list)
    game_draw = draw(game_list)

    if game_draw == True:
        game_fini = True
        print("Its a draw")

    if game_fini == True and game_draw == False:
        winner = moves_list[-1]
        print(f'Player {winner} won!')

print(moves_list)
