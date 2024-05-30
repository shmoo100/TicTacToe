import csv

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output


boards = getCSVtoList('data_test_minmax.txt')

moves = []

for i in boards:
    moves.append(i[0])

print(moves)
