def initial_state():
    return [['', '', ''], ['', '', ''], ['', '', '']]

def player(board):
    if sum(row.count('') for row in board) % 2 == 1:
        return 'X'
    return 'O'

def actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']

def result(board, action):
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    # Horizontal, vertical, and diagonal checks
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combination in win_combinations:
        x, y, z = combination
        if board[x[0]][x[1]] == board[y[0]][y[1]] == board[z[0]][z[1]] != '':
            return board[x[0]][x[1]]
    return None

def terminal(board):
    return winner(board) is not None or all(cell != '' for row in board for cell in row)

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == 'X':
        best_value = float('-inf')
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def utility(board):
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    # Your game initialization code here
    # Example: start_game()
