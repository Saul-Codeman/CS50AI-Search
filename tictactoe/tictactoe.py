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
    if board == initial_state():
        return X
    else:
        x_count = sum(row.count(X) for row in board)
        o_count = sum(row.count(O) for row in board)
        if o_count < x_count:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
               actions.add((i, j)) 
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Determine player
    current_player = player(board)
    # Create deep copy of board
    board_copy = copy.deepcopy(board)
    
    if board_copy[action[0]][action[1]] == EMPTY:
        board_copy[action[0]][action[1]] = current_player
    else:
        raise ValueError("Invalid move: Cell is not empty")
    
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == X for j in range(3)):
            return X
        if all(board[j][i] == X for j in range(3)):
            return X
        if all(board[i][j] == O for j in range(3)):
            return O
        if all(board[j][i] == O for j in range(3)):
            return O
    if all(board[i][i] == X for i in range(3)):
        return X
    if all(board[i][2 - i] == X for i in range(3)):
        return X
    if all(board[i][i] == O for i in range(3)):
        return O
    if all(board[i][2 - i] == O for i in range(3)):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Could eventually modify using alpha beta pruning
    # Define min and max value
    def max_value(board):
        v = -float('inf')
        if terminal(board):
            return None, utility(board)

        best_action = None
    
        for action in actions(board):
            _, minimum_val = min_value(result(board, action))
            if minimum_val > v:
                v = minimum_val
                best_action = action
                
        return best_action, v
    
        
    def min_value(board):
        v = float('inf')
        if terminal(board):
            return None, utility(board)
        
        worst_action = None
    
        for action in actions(board):
            _, maximum_val = max_value(result(board, action))
            if maximum_val < v:
                v = maximum_val
                worst_action = action
                
        return worst_action, v
    
    # GO down different minimax routes if player is X(max) or O(min).
    current_player = player(board)
    if current_player == X:
        optimal_action, v = max_value(board)
    else:
        optimal_action, v = min_value(board)
    return optimal_action

        
    
