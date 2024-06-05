import csv


characters = [1, 0, -1]

def collect_data(file,data):
    with open(file,'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(data)

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

def generate_possible_states(li, length):

    if length == 0:
        o = li.count(1)
        x = li.count(-1)
        empty = li.count(0)

        if (o-x == 1 or o-x == 0) and empty > 0:
            if check(li) == 0:
                collect_data('possible_states.txt', li)
        return
    for i in characters:
        generate_possible_states(li + [i], length - 1)


generate_possible_states([], 9)
