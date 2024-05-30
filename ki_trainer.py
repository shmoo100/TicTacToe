from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
import csv

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output

trainX = getCSVtoList('data_test.txt')
trainY = []

k = getCSVtoList('data_test_minmax.txt')
for i in k:
    trainY.append(i[0])

print(trainX)
print(trainY)