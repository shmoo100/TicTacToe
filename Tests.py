import csv


def collect_data(file,data):
    with open(file,'a',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(data)

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output


k = getCSVtoList('best_move.txt')
y = []
for i in k:
    y.append(i[0])


print(y)