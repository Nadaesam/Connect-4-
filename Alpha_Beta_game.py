from Alpha_Beta_board import Board
import time
import copy

# GAME LINK
# http://kevinshannon.com/connect4/

EMPTY = 0
RED = 1
BLUE = 2

def is_valid_move(board, column):
    return board[5][column] == EMPTY

def evaluate_window(window):
    score = 0
    if window.count(RED) == 4:
        score += 100
    elif window.count(RED) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(RED) == 2 and window.count(0) == 2:
        score += 2
    if window.count(BLUE) == 4:
        score -= 100
    elif window.count(BLUE) == 3 and window.count(0) == 1:
        score -= 5
    elif window.count(BLUE) == 2 and window.count(0) == 2:
        score -= 2
    return score

def evaluate_board(board):
    score = 0
    
    # Check rows for winning moves
    for row in range(6):
        for col in range(4):
            window = board[row][col:col+4]
            score += evaluate_window(window)

    # Check columns for winning moves
    for col in range(7):
        for row in range(3):
            window = [board[i][col]for i in range(row, row+4)]
            score += evaluate_window(window)

    # Check diagonal (positive slope) for winning moves
    for row in range(3):
        for col in range(4):
            window = [board[row+i][col+i] for i in range(4)]
            score += evaluate_window(window)

    # Check diagonal (negative slope) for winning moves
    for row in range(3, 6):
        for col in range(4):
            window = [board[row-i][col+i] for i in range(4)]
            score += evaluate_window(window)

    # Count the number of open winning moves for each player
    red_moves = count_open_winning_moves(board, RED)
    blue_moves = count_open_winning_moves(board, BLUE)
    
    # Add the difference in open winning moves to the score
    score += 5 * (red_moves - blue_moves)
    
    return score

def count_open_winning_moves(board, player):
    count = 0
    
    # Check rows for open winning moves
    for row in range(6):
        for col in range(4):
            window = board[row][col:col+4]
            if window.count(player) == 3 and window.count(0) == 1:
                count += 1

    # Check columns for open winning moves
    for col in range(7):
        for row in range(3):
            window = [board[i][col] for i in range(row, row+4)]
            if window.count(player) == 3 and window.count(0) == 1:
                count += 1

    # Check diagonal (positive slope) for open winning moves
    for row in range(3):
        for col in range(4):
            window = [board[row+i][col+i] for i in range(4)]
            if window.count(player) == 3 and window.count(0) == 1:
                count += 1

    # Check diagonal (negative slope) for open winning moves
    for row in range(3, 6):
        for col in range(4):
            window = [board[row-i][col+i] for i in range(4)]
            if window.count(player) == 3 and window.count(0) == 1:
                count += 1
    
    return count

def make_move(board, col, player):
    temp_board = copy.deepcopy(board)
    for row in range(5, -1, -1):
        if temp_board[row][col] == 0:
            temp_board[row][col] = player
            return temp_board

def main(depth):
    board = Board()

    time.sleep(3)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE

        def minimax(board, depth, maximizing_player, alpha, beta):
            if depth == 0:
                return None, evaluate_board(board)

            if maximizing_player:
                max_eval = float('-inf')
                max_col = None
                for col in range(7):
                    if not is_valid_move(board, col):
                        continue
                    temp_board = make_move(board, col, RED)
                    _, eval_score = minimax(temp_board, depth - 1, False, alpha, beta)
                    if eval_score > max_eval:
                        max_eval = eval_score
                        max_col = col
                    elif eval_score == max_eval:
                        # Choose the move with more open winning moves
                        if count_open_winning_moves(temp_board, RED) > count_open_winning_moves(board, RED):
                            max_col = col
                    alpha = max(alpha, eval_score)
                    if alpha >= beta:
                        break
                return max_col, max_eval

            else:
                min_eval = float('inf')
                min_col = None
                for col in range(7):
                    if not is_valid_move(board, col):
                        continue
                    temp_board = make_move(board, col, BLUE)
                    _, eval_score = minimax(temp_board, depth - 1, True, alpha, beta)
                    if eval_score < min_eval:
                        min_eval = eval_score
                        min_eval = col
                    beta = min(beta, eval_score)
                    if alpha >= beta:
                        break
                return min_col, min_eval

        # Use minimax to select the best column
        column, _ = minimax(game_board, depth=depth , maximizing_player=True, alpha=float('-inf'), beta=float('inf'))
        if column is not None:
            board.select_column(column)
        time.sleep(3)


if __name__ == "__main__":
    main(depth=5)