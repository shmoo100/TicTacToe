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
    model.add(Dense(9, input_shape=(9,), kernel_initializer='normal',activation='relu'))
    model.add(Dense(9,kernel_initializer='normal', activation='softmax'))
    model.compile(loss='mean_squared_error',optimizer='SGD', metrics=['accuracy'])
    return model




liX = getCSVtoList('board_states.txt')
liY = []

k = getCSVtoList('best_move.txt')
for i in k:
    liY.append(i[0])

mid_indexX = len(liX) // 2
mid_indexY = len(liY) // 2

testX = np.array(liX[mid_indexX:])
testY = np.array(liY[mid_indexY:])

trainX = np.array(liX[:mid_indexX])
trainY = np.array(liY[:mid_indexY])



trainY = to_categorical(trainY)
testY = to_categorical(testY)

model = nn_model()
model.summary()

history = model.fit(trainX, trainY, epochs=1000, batch_size=100, verbose=1)
model.save('model_trained_script.keras')
scores = model.evaluate(testX, testY, verbose=1)
print("Baseline Accuracy: %.2f%%" % (scores[1] * 100))
print("Baseline Loss: %.2f%%" % (scores[0] * 100))


# Modell evaluieren
figure, axis = plt.subplots(1, 2)
axis[0].plot(history.history['accuracy'])
axis[0].set_title('model accuracy')
axis[0].set_ylabel('accuracy')
axis[0].set_xlabel('epoch')
axis[0].legend(['train', 'test'], loc='upper left')

axis[1].plot(history.history['loss'])
axis[1].set_title('model loss')
axis[1].set_ylabel('loss')
axis[1].set_xlabel('epoch')
axis[1].legend(['train', 'test'], loc='upper left')

plt.show()
