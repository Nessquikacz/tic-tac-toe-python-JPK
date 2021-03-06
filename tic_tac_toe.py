import os

def logo_tictactoe():
    logo ='''
 _   _      _             _             
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ \\
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|'''
    print(logo)


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.', '.', '.', ],
             ['.', '.', '.', ],
             ['.', '.', '.', ]]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""

    

    row, col = 0, 0
    valid_numbers = ['1', '2', '3']
    valid_letters = ['a', 'b', 'c']
    valid_inputs = ['a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3']
    is_valid_input = False

    # repetitively ask for valid input of the position
    while not is_valid_input:

        # converts string into list

        user_input = list(input('Please provide coordinate: '))

        # invalid input if more than 2 characters
        if len(user_input) > 2:
            print('Invalid coordinate, please try again')
        else:
            # checks if input is in valid is in valid inputs list
            if user_input[0] in valid_inputs and user_input[1] in valid_inputs:
                # if item is alpha then row, if numeric then column
                for inp in user_input:
                    if inp.isalpha():
                        # assign index of the position in valid_letters to row as coordinate in board
                        row = valid_letters.index(inp.lower())
                    elif inp.isnumeric():
                        # assign index of the position in valid_numbers to col as coordinate in board
                        col = valid_numbers.index(inp)

                        # checks if the position if free to take
                        if board[row][col] == '.':
                            is_valid_input = True
                        else:
                            print('Wrong move, try again')

            else:
                print('Invalid coordinate, please try again')

    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    # check whose turn it is and if given cell is empty it puts the mark inside
    if player.lower() == 'x' and board[row][col] == '.':
        board[row][col] = 'X'
    elif player.lower() == 'o' and board[row][col] == '.':
        board[row][col] = 'O'
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    win = False

    for i in range(3):
        # horizontal wins
        if board[i][0] == board[i][1] == board[i][2] == player:
            win = True
        # vertical wins
        elif board[0][i] == board[1][i] == board[2][i] == player:
            win = True
    # diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        win = True

    return win
       


def is_full(board):
    """Returns True if board is full."""
    all_cells = len(board[0]) * len(board)
    taken_cells = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '.':
                taken_cells += 1

    if taken_cells == all_cells:
        return True
    else:
        return False


def print_board(board):

    full_board = (f'''   1   2   3
A  {board[0][0]} | {board[0][1]} | {board[0][2]}
  ---+---+---
B  {board[1][0]} | {board[1][1]} | {board[1][2]}
  ---+---+---
C  {board[2][0]} | {board[2][1]} | {board[2][2]}''')

    print(full_board)


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 'X':
        print('Congratulations player X! You won!')
    elif winner == 'O':
        print('Congratulations player O! You won!')
    elif winner == 0:
        print('Tie!')


def game_menu():
    logo_tictactoe()
       
    print('''\nGame Rules:
    1. First player is an X, second player is an O.
    2. Player pick a coordinate on the board, trying to create diagonal/vertical/horizonal line.
    3. First player to create a line with their mark wins.
    4. In case of whole board getting filled without previous win, there is a tie.
    5. Have fun!''')  

    levels = ['1', '2', '3', '4']
    while True:
        mode = input('''\nChoose your game mode 
        1 - Easy mode (3x3 board)
        2 - Hard mode (5x5 board)
        3 - Fun mode (Find out :) )
        4 - vs AI 
        ''')

        if mode in levels:
            return mode
        else:
            print('Provide valid level.')      
    


def tictactoe_game(mode='HUMAN-HUMAN'):

    full_board = False
    player_x = 'X'
    player_o = 'O'
    board = init_board()
    print_board(board)
    row_x, col_x = get_move(board, player_x)
    marked_board = mark(board, player_x, row_x, col_x)
    x_won = has_won(marked_board, player_x)
    o_won = has_won(marked_board, player_o)
    print_board(marked_board)    

    while x_won == False and is_full(marked_board) == False and o_won == False:
        row_o, col_o = get_move(marked_board, player_o)
        marked_board = mark(marked_board, player_o, row_o, col_o)
        print_board(marked_board)
        o_won = has_won(marked_board, player_o)
        
        if o_won == True:
            winner = 'O'
            print_result(winner)   
            break

        row_x, col_x = get_move(marked_board, player_x)
        marked_board = mark(marked_board, player_x, row_x, col_x)
        print_board(marked_board)
        x_won = has_won(marked_board, player_x)

        if x_won == True:
            winner = 'X'
            print_result(winner)  
            break

        full_board = is_full(marked_board)
        if full_board == True:
            winner = 0
            print_result(winner)


def main_menu():
    game_menu()
    os.system('cls')
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
