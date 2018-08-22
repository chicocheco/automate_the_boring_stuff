the_board = {'from_top-L': ' ', 'from_top-M': ' ', 'from_top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):  # 'board' in here is just a name of the argument, you can pass any dictionary to it,
    # 'the_board' is just one of them
    print(board['from_top-L'] + '|' + board['from_top-M'] + '|' + board['from_top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'  # the player 'X' always starts...
for i in range(9):  # loop runs 9 times
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()  # you have to pass a key-value from 'the_board' dictinary
    the_board[move] = turn  # assign either X or O to the particular key-value (now empty) of the dictionary (the one you typed)
    if turn == 'X':  # if turn is X the change (assign) turn to O
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)
