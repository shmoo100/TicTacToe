# Die Daten sind als mnist in tensorflow gespeichert.
# mnist muss daher importiert werden.
from tensorflow.keras.datasets import mnist

# zum Darstellen der Daten wird matplotlib verwendet
from matplotlib import pyplot as plt

# Datenset wird geladen. Trainings- und Testdaten werden aufgeteilt.
(trainX, trainY), (testX, testY) = mnist.load_data()

# Zusammenfassung des geladenen Datensets
print('Train: X=%s, y=%s' % (trainX.shape, trainY.shape))
print('Test: X=%s, y=%s' % (testX.shape, testY.shape))

#plotte die ersten 16 Bilder
for i in range(16):
    # Erstelle die Subplots. Pro Bild muss ein Subplot erstellt werden
    plt.subplot(4,4,i+1)
    # Zeige die Bilder in schwarz-weiss.
    plt.imshow(trainX[i], cmap=plt.get_cmap('gray'))

# Gib die Labels der dargestellten Bilder aus.
for i in range(16):
    print( "i=",i," Ziffer=",trainY[i])
# Zeige die ersten 16 Bilder
plt.show()
print(type(trainY))
