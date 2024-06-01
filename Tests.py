import keras.models
import numpy as np


def getMoveAI(model, board):
    inArray = np.array(board)
    inArray = inArray.reshape(1, 9)
    pred = list(model.predict(inArray))

    return pred

model=keras.models.load_model('model_trained_script.keras')
board=[0, 0, 0, 0, 0, 0, 0, 0, 0]
AIReturn = getMoveAI(model, board)

print(AIReturn)
max_value = max(AIReturn[0])
print(max_value)
AiValues = AIReturn[0].tolist()
AiMove = AiValues.index(max_value)
print(AiMove)