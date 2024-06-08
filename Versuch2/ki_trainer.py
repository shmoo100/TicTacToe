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
    model.add(Dense(729, input_shape=(9,), kernel_initializer='normal',activation='tanh'))
    model.add(Dense(81, kernel_initializer='normal', activation='tanh'))
    model.add(Dense(9,kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam', metrics=['accuracy'])
    return model




liX = getCSVtoList('possible_states.txt')


k = getCSVtoList('possible_states_moves.txt')
liY = []


for i in k:
    liY.append(i[0])


trainX = np.array(liX)
trainY = np.array(liY)


trainY = to_categorical(trainY)

model = nn_model()
model.summary()

history = model.fit(trainX, trainY, epochs=250, batch_size=50, verbose=1)
model.save('model_tictactoe_end.keras')



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
