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

        print('Provide input')
        # converts string into list

        user_input = list(input())

        # invalid input if more than 2 characters
        if len(user_input) > 2:
            print('Invalid input, try again')
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
                print('Invalid input, try again')

    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    # check whose turn it is and if given cell is empty it puts the mark inside
    # check whose turn it is and if given cell is empty it puts the mark inside
    if player.lower() == 'x' and board[row][col] == '.':
        board[row][col] = 'X'
    elif player.lower() == 'o' and board[row][col] == '.':
        board[row][col] = 'O'
    return board


# def has_won(board, player):
#     """Returns True if player has won the game."""
#     pass
#     # soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
#     '''#checks if player has three of their marks horizonally
#     for x in range(len(board)):
#         win = True
          
#         for y in range(len(board)):
#             if board[x, y] != player:
#                 win = False
#                 continue
                  
#         if win == True:
#             return(win)

#     #checks if player has three of their marks vertically
#     elif for x in range(len(board)):
#         win = True
          
#         for y in range(len(board)):
#             if board[y][x] != player:
#                 win = False
#                 continue
                  
#         if win == True:
#             return(win)
    
#     #checks if player has three of their marks diagonally'''
#     # return False


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


# board = {'A1': ' . ' , 'A2': ' . ' , 'A3': ' . ' ,
#         'B1': ' . ' , 'B2': ' . ' , 'B3': ' . ' ,
#         'C1': ' . ' , 'C2': ' . ' , 'C3': ' . '}
def print_board(board):


    print('   ' + '1' + '   ' + '2' + '   ' + '3')
    print('A ' + board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print("  ---+---+---")
    print('B ' + board[1][0] + '|' + board[1][1]+ '|' + board[1][2])
    print("  ---+---+---")
    print('C ' + board[2][0] + '|' + board[2][1] + '|' + board[2][2])


board = init_board()


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
