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
        print('Congratulations player x! You won!')
    elif winner == 'O':
        print('Congratulations player O! You won!')
    elif winner == 0:
        print('Tie!')


def tictactoe_game(mode='HUMAN-HUMAN'):

    full_board = False
    board = init_board()
    print_board(board)
    row_x, col_x = get_move(board, 'X')
    marked_board = mark(board, 'X', row_x, col_x)
    x_won = has_won(marked_board, 'X')
    o_won = has_won(marked_board, 'O')
    print_board(marked_board)
    

    while x_won == False and is_full(marked_board) == False and o_won == False:
        row_o, col_o = get_move(marked_board, 'O')
        marked_board = mark(marked_board, 'O', row_o, col_o)
        print_board(marked_board)
        o_won = has_won(marked_board, 'O')
        full_board = is_full(marked_board)


        row_x, col_x = get_move(marked_board, 'X')
        marked_board = mark(marked_board, 'X', row_x, col_x)
        print_board(marked_board)
        x_won = has_won(marked_board, 'X')
        full_board = is_full(marked_board)

       
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    # print_board(board)
    #row, col = get_move(board, 1)
    #mark(board, 1, row, col)

    #winner = 0
    # print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
