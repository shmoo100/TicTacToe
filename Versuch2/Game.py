import keras.models
import numpy as np


def getMoveAI(model, board):
    inArray = np.array(board)
    inArray = inArray.reshape(1, 9)
    pred = list(model.predict(inArray))

    return pred

def print_board(board):

    board2 = list(board)
    for j in range(0, 9):
        if board2[j] == 1:
            board2[j] = "0"
        elif board2[j] == -1:
            board2[j] = "X"
        else:
            board2[j] = " "

    for i in range(0, 3):
        print(str(board2[3 * i]) + "|" + str(board2[3 * i + 1]) + "|" + str(board2[3 * i + 2]))
        print('-' * 5)


def check(feld):

    x = 0
    for i in range(0, 3):
        if feld[3*i] == feld[3*i+1] and feld[3*i+1] == feld[3*i+2] and feld[3*i] != 0:
            x = feld[3*i]

    for i in range(0, 3):
        if feld[i] == feld[i + 3] and feld[i + 3] == feld[i + 6] and feld[i] != 0:
            x = feld[i]

    if feld[0] == feld[4] and feld[4] == feld[8] and feld[0] != 0:
        x = feld[0]

    if feld[2] == feld[4] and feld[4] == feld[6] and feld[4] != 0:
        x = feld[4]

    return x


board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

winner = 0
player = 1
turn = 1
model = keras.models.load_model('model_tictactoe_end.keras')
AiPlayer = int(input("Soll AI beginnen ? (1 = Ja / -1 = Nein)"))
while AiPlayer != 1 and AiPlayer != -1:
    AiPlayer = int(input("Soll AI beginnen ? (1 = Ja / -1 = Nein)"))


while winner == 0 and turn != 10:

    print_board(board)

    if player == AiPlayer or 3 == AiPlayer:
        AiReturn = getMoveAI(model, board)
        AiReturn = AiReturn[0].tolist()
        max_value = max(AiReturn)
        playerIn = AiReturn.index(max_value)
        if board[playerIn] != 0:

            print("illegal move by AI")
            print(playerIn)
            print(AiReturn)
            break


    else:

        playerIn = int(input("Gib ein leeres Feld ein (1-9)"))-1

        while board[playerIn] != 0 or playerIn < 0:
            playerIn = int(input("Gib ein leeres Feld ein (1-9)"))-1


    board[playerIn] = player

    winner = check(board)
    turn += 1
    player = player*-1


print_board(board)


if winner == 1:
    print("O won")
elif winner == -1:
    print("X won")
else:
    print("tie")



