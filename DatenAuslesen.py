import csv

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output


boards = getCSVtoList('data_test.txt')

for i in boards:
    print(i)