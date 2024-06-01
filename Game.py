import keras.models
import numpy as np


def getMoveAI(model, board):
    inArray = np.array(board)
    inArray = inArray.reshape(1, 9)
    pred = list(model.predict(inArray))

    return pred


def korrektur(feld):

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
model = keras.models.load_model('model_trained_script.keras')
AiPlayer = int(input("Soll AI beginnen?"))


while winner == 0 and turn != 10:

    for i in range(0, 3):
        print(str(board[3 * i]) + "|" + str(board[3 * i + 1]) + "|" + str(board[3 * i + 2]))

    if player == AiPlayer:
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

        playerIn = int(input("Gib eine leeres Feld ein"))-1

        while board[playerIn] != 0 or playerIn < 0:
            player = int(input("Gib eine leeres Feld ein"))-1


    board[playerIn] = player

    winner = korrektur(board)
    turn += 1
    player = (player % 2) + 1


print(winner)



