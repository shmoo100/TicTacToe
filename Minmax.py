import math
import csv

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output

def collect_data(file,data):
    with open(file,'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(data)

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check if a player has won
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

# Check for a tie
def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Get available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            best_score = min(score, best_score)
        return best_score

# Find the best move
def find_best_move(board, player):
    best_score = -math.inf if player == 'O' else math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = player
        score = minimax(board, 0, player == 'X')
        board[move[0]][move[1]] = ' '
        if player == 'O':
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move
    return best_move

# Main function to get the best move for a given board state
def get_best_move_for_current_state(board, current_player):
    move = find_best_move(board, current_player)
    return move

# Example usage
if __name__ == "__main__":

    boards = getCSVtoList('board_states.txt')

    for k in boards:
        feld = list(k)


        if (feld.count(1) == feld.count(-1)):
            current_player = 'O'
        else:
            current_player = 'X'

        for i in range(0, 9):

            if feld[i] == 1:
                feld[i] = '0'

            elif feld[i] == 0:
                feld[i] = ' '

            else:
                feld[i] = 'X'


        board = [
            [feld[0], feld[1], feld[2]],
            [feld[3], feld[4], feld[5]],
            [feld[6], feld[7], feld[8]]
        ]

        best_move = get_best_move_for_current_state(board, current_player)
        numberBM = best_move[0]*3 + best_move[1]
        print(numberBM)
        li = [numberBM]
        collect_data('best_move.txt', li)

