"""
Name: Thomas Scola
lab9.py
Certification of Authenticity:
I worked on this assignment with Brooke Duvall at the CSL tutoring center.
"""


def build_board():
    board = [1,2,3,4,5,6,7,8,9]
    return board
    pass


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(board[position-1]).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    board[position-1] = character

    pass

def game_is_won(board):
    if board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[6] == board[4] == board[2]:
        return True
    else:
        return False
    pass

def winning_game(board):
    if game_is_won(board):
        return True
    else:
        return False
    pass

def game_over(board):
    if game_is_won(board):
        return True
    x = 0
    for i in board:
        if not i.isnumeric():
            x = x + 1
    if x == 9:
        return True
    return False

    pass

def get_winner(board):
    if board[0] == board[3] == board[6] == 'x':
        return 'x'
    elif board[1] == board[4] == board[7] == 'x':
        return 'x'
    elif board[2] == board[5] == board[8] == 'x':
        return 'x'
    elif board[0] == board[1] == board[2] == 'x':
        return 'x'
    elif board[3] == board[4] == board[5] == 'x':
        return 'x'
    elif board[6] == board[7] == board[8] == 'x':
        return 'x'
    elif board[0] == board[4] == board[8] == 'x':
        return 'x'
    elif board[6] == board[4] == board[2] == 'x':
        return 'x'
    elif board[0] == board[3] == board[6] == 'o':
        return 'o'
    elif board[1] == board[4] == board[7] == 'o':
        return 'o'
    elif board[2] == board[5] == board[8] == 'o':
        return 'o'
    elif board[0] == board[1] == board[2] == 'o':
        return 'o'
    elif board[3] == board[4] == board[5] == 'o':
        return 'o'
    elif board[6] == board[7] == board[8] == 'o':
        return 'o'
    elif board[0] == board[4] == board[8] == 'o':
        return 'o'
    elif board[6] == board[4] == board[2] == 'o':
        return 'o'
    else:
        return None
    pass


def play(board):
    x_turn = True
    char = "x"
    while not game_over(board):
        print_board(board)
        if x_turn:
            pos = eval(input('x position'))
            char = "x"
        else:
            pos = eval(input('o position'))
            char = "o"
        if is_legal(board, pos):
            fill_spot(board, pos, char)
            x_turn = not x_turn

    get_winner(board)



def main():
    pass


if __name__ == '__main__':
    main()
