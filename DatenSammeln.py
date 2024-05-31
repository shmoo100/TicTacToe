from random import randint
import csv


def collect_data(file,data):
    with open(file,'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(data)

def korrektur(feld):

    x = 0
    for i in range(0, 3):
        if feld[3*i] == feld[3*i+1] == feld[3*i+2] and feld[3*i] != 0:
            x = feld[3*i]

    for i in range(0, 3):
        if feld[i] == feld[i + 3] == feld[i + 6] and feld[i] != 0:
            x = feld[i]

    if feld[0] == feld[4] == feld[8] and feld[0] != 0:
        x = feld[4]

    if feld[2] == feld[4] == feld[6] and feld[4] != 0:
        x = feld[4]

    return x

for i in range(0, 2):

    feld = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    winner = 0
    player = 1
    turn = 1


    while winner == 0 and turn != 10:

        collect_data('board_states.txt', feld)

        if len(inputs) > 1:
            playerIn = inputs[randint(0, len(inputs)-1)]
            inputs.remove(playerIn)
        else:
            playerIn = inputs[0]

        feld[playerIn] = player

        winner = korrektur(feld)
        turn += 1
        player = player * -1










