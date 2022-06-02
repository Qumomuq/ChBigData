from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    >>> tic_tac_toe_checker([['x', '0', '0'],['x', '0', 'x'],['x', 'x', '0']]) # victory х
    'x wins'
    >>> tic_tac_toe_checker([['0', '0', '0'],['x', '0', 'x'],['x', 'x', '0']]) # victory 0
    '0 wins'
    >>> tic_tac_toe_checker([['-', '0', '0'],['x', '0', '-'],['x', 'x', '0']]) # the game is not over
    'the board is unfinished'
    >>> tic_tac_toe_checker([['0', '0', 'x'],['x', 'x', '0'],['0', 'x', '0']]) # draw
    "it's a draw"
    """
    who = ''
    res = False
    for i in range(3):  # проверяем равны ли элементы в колоннах и строках
        if board[i][0] == board[i][1] == board[i][2]:
            res = True
            who = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i]:
            res = True
            who = board[0][i]
            break

    if (board[0][0] == board[1][1] == board[2][2]) or (
            board[0][2] == board[1][1] == board[2][0]):  # равны ли элементы по диагоналям
        res = True
        who = board[1][1]

    if res:
        return f'{who} wins'
    else:
        joined_list = board[0] + board[1] + board[2]
        if '-' in joined_list:
            return 'the board is unfinished'
        else:
            return "it's a draw"
