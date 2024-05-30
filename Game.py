feld = [0, 0, 0, 0, 0, 0, 0, 0, 0]

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


winner = 0
player = 1
turn = 1


while winner == 0 and turn != 10:

    for i in range(0, 3):
        print(str(feld[3 * i]) + "|" + str(feld[3 * i + 1]) + "|" + str(feld[3 * i + 2]))

    playerIn = int(input("Gib eine leeres Feld ein"))-1
    print(playerIn)

    while feld[playerIn] != 0 or playerIn < 0:
        player = int(input("Gib eine leeres Feld ein"))-1

    feld[playerIn] = player

    winner = korrektur(feld)
    turn += 1
    player = (player % 2) + 1


print(winner)



