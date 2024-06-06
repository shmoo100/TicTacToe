import csv

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output

def collect_data(file,data):
    with open(file,'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(data)



def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_draw(board):
    return all(cell != 0 for cell in board)


def minimax(board, depth, is_maximizing):
    if is_winner(board, 1):
        return 10 - depth
    if is_winner(board, -1):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = minimax(board, depth + 1, False)
                board[i] = 0
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = -1
                score = minimax(board, depth + 1, True)
                board[i] = 0
                best_score = min(best_score, score)
        return best_score


def find_best_move(board):
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = minimax(board, 0, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    return best_move



boards = getCSVtoList('possible_states.txt')
boards_number = len(boards)
boards_done = 0

for k in boards:
    best_move = find_best_move(k)
    li = [best_move]
    collect_data('possible_states_moves.txt', li)

    boards_done += 1

    if boards_done % 50 == 0:
        print(str(boards_done/boards_number))
