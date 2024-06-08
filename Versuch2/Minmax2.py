import csv

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output

def collect_data(file,data):
    with open(file,'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(data)


def check_for_winner(board):

    x = 0
    for i in range(0, 3):
        if board[3 * i] == board[3 * i + 1] and board[3 * i + 1] == board[3 * i + 2] and board[3 * i] != 0:
            x = board[3 * i]

    for i in range(0, 3):
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i] != 0:
            x = board[i]

    if board[0] == board[4] and board[4] == board[8] and board[0] != 0:
        x = board[0]

    if board[2] == board[4] and board[4] == board[6] and board[4] != 0:
        x = board[4]

    return x

def minimax(board, depth, player):

    winner = check_for_winner(board)
    if winner == 1:
        return 10-depth
    elif winner == -1:
        return depth-10
    elif winner == 0 and board.count(0) == 0:
        return 0

    if player == 1:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = minimax(board, depth + 1, -1)
                board[i] = 0
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = -1
                score = minimax(board, depth + 1, 1)
                board[i] = 0
                best_score = min(best_score, score)
        return best_score

def find_best_move(board, player, turn):
    best_move = -1
    if player == 1:
        best_score = -float('inf')
    elif player == -1:
        best_score = float('inf')

    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score = minimax(board, turn, -player)
            board[i] = 0

            if player == 1 and score > best_score:
                best_score = score
                best_move = i
            elif player == -1 and score < best_score:
                best_score = score
                best_move = i

    return best_move




boards = getCSVtoList('possible_states.txt')
boards_number = len(boards)
boards_done = 0

for k in boards:

    if k.count(1) == k.count(-1):
        player = 1
    else:
        player = -1

    turn = k.count(1) + k.count(-1)
    best_move = find_best_move(k, player, turn)
    li = [best_move]
    collect_data('possible_states_moves.txt', li)

    boards_done += 1

    if boards_done % 50 == 0:
        print(str(boards_done/boards_number))

