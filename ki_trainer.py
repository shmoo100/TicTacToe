from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
import numpy as np
import csv

def getCSVtoList(file):
    with open(file,'r') as f:
        output=list(csv.reader(f,quoting=csv.QUOTE_NONNUMERIC))
    return output

def nn_model():
    model=Sequential()
    model.add(Dense(9, input_shape=(9,), kernel_initializer='normal',activation='sigmoid'))
    model.add(Dense(9,kernel_initializer='normal', activation='softmax'))
    model.compile(loss='mean_squared_error',optimizer='SGD', metrics=['accuracy'])
    return model




liTrainX = getCSVtoList('data_test.txt')
liTrainY = []

k = getCSVtoList('data_test_minmax.txt')
for i in k:
    liTrainY.append(i[0])

liTrainX2 = [[int(item) for item in sublist] for sublist in liTrainX]
liTrainY2 = [int(item) for item in liTrainY]

trainX = np.array(liTrainX2)
trainY = np.array(liTrainY2)
testX = trainX
testY = trainY

print(trainX)
print(trainY)

trainY = to_categorical(trainY)
testY = to_categorical(testY)

model = nn_model()
model.summary()

model.fit(trainX, trainY, epochs=10, batch_size=20, verbose=1)
model.save('model_trained.keras')
scores=model.evaluate(testX, testY, verbose=1)
print("Baseline Accuarcy: %.2f%%"%(scores[1]*100))
