import copy
import math

def initial_state():
    board = [[None for _ in range(3)] for _ in range(3)]
    return board

def player(state):
    letter = ""
    x = sum(row.count("X") for row in state)
    o = sum(row.count("O") for row in state)
    if x == o:
        letter = "X"
    else:
        letter = "O"

    return letter 

def actions(state):
    available_moves = [(i,j) for i, row in enumerate(state) for j, elm in enumerate(row) if elm is None]
    return available_moves

def result(state, action):
    board = copy.deepcopy(state)
    i, j = action
    if board[i][j] is not None:
        raise Exception("Cell must be empty to make a move")
    letter = player(state)
    board[i][j] = letter
    return board

def winner(state):
    for i, board in enumerate(state):
        #Horizontal wins
        if all(state[i][j] == "X" for j in range(3)):
            return "X"
        elif all(state[i][j] == "O" for j in range(3)):
            return "O"
        #Vertical wins
        if all(state[j][i] == "X" for j in range(3)):
            return "X"
        elif all(state[j][i] == "O" for j in range(3)):
            return "O"
    #Diagonal wins
    for player in ("X", "O"):
        diagonal_1 = all(state[j][j] == player for j in range(3)) 
        diagonal_2 = all(state[j][2-j] == player for j in range(3))
        if diagonal_1 or diagonal_2:
            return player
    return None

def terminal(state):
    if winner(state):
        return True
    elif all(col is not None for row in state for col in row):
        return True
    return False

def utility(state):
    letter = winner(state)
    if letter == "X":
        return 1
    elif letter == "O":
        return -1
    return 0

def minimax(state):
    if terminal(state):
        return None
    letter = player(state)
    if letter == "X":
        best_value = -math.inf
        for action in actions(state):
            v = min_value(result(state, action))
            if v > best_value:
                best_value = v
                best_mov = action

    if letter == "O":
        best_value = math.inf
        for action in actions(state):
            v = max_value(result(state, action))
            if best_value > v:
                best_value = v
                best_mov = action
    return best_mov
        

def max_value(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v

def min_value(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v