"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0
    for r in range(3):
        for c in range(3):
            if (board[r][c] == X):
                numX += 1
            elif (board[r][c] == O):
                numO += 1
    if numX == numO:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for r in range(3):
        for c in range(3):
            if (board[r][c] == EMPTY):
                result.add((r, c))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    if action not in actions(board=board):
        raise ValueError

    (i, j) = action
    curPlayer = player(board=board)
    result[i][j] = curPlayer
    return result


def hasWinner(board):
    for r in range(3): # check 3 rows
        if board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0] != None:
            return board[r][0]

    for c in range(3): # check 3 columns
        if board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[0][c] != None:
            return board[0][c]

    # check 2 diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][2]


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if hasWinner(board=board) != None:
        return hasWinner(board=board)
    return None # no winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if hasWinner(board=board) != None:
        return True
    
    numFilled = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] != None:
                numFilled += 1

    if numFilled == 9: # tie
        return True
    
    return False


def utility(board): # board is Terminal
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = hasWinner(board=board)
    if winner == None:
        return 0
    if winner == X:
        return 1
    return -1


def max_value(board):
    if terminal(board=board):
        return utility(board=board)
    val = -math.inf
    for action in actions(board=board):
        val = max(val, min_value(result(board=board, action=action)))
    return val


def min_value(board):
    if terminal(board=board):
        return utility(board=board)
    val = math.inf
    for action in actions(board=board):
        val = min(val, max_value(result(board=board, action=action)))
    return val


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curPlayer = player(board=board)
    resultAction = None

    if curPlayer == X:
        maxVal = -math.inf
        for action in actions(board=board):
            if maxVal < min_value(result(board=board, action=action)):
                resultAction = action
                maxVal = min_value(result(board=board, action=action))
    else:
        minVal = math.inf
        for action in actions(board=board):
            if minVal > max_value(result(board=board, action=action)):
                resultAction = action
                minVal = max_value(result(board=board, action=action))

    return resultAction
