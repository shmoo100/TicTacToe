import keras.models
import numpy as np
import tkinter as tk
from tkinter import messagebox

def getMoveAI(model, board):
    inArray = np.array(board)
    inArray = inArray.reshape(1, 9)
    pred = list(model.predict(inArray))
    return pred

def check(feld):
    for i in range(3):
        if feld[3*i] == feld[3*i+1] and feld[3*i+1] == feld[3*i+2] and feld[3*i] != 0:
            return feld[3*i]
    for i in range(3):
        if feld[i] == feld[i+3] and feld[i+3] == feld[i+6] and feld[i] != 0:
            return feld[i]
    if feld[0] == feld[4] and feld[4] == feld[8] and feld[0] != 0:
        return feld[0]
    if feld[2] == feld[4] and feld[4] == feld[6] and feld[4] != 0:
        return feld[4]
    return 0

def update_board():
    for i in range(9):
        if board[i] == 1:
            buttons[i].config(text="O")
        elif board[i] == -1:
            buttons[i].config(text="X")
        else:
            buttons[i].config(text=" ")

def on_button_click(index):
    global player, winner, turn
    if board[index] == 0 and winner == 0:
        board[index] = player
        winner = check(board)
        turn += 1
        player *= -1
        update_board()
        if winner != 0 or turn == 10:
            end_game()
        elif player == AiPlayer:
            ai_move()

def ai_move():
    global player, winner, turn
    AiReturn = getMoveAI(model, board)
    AiReturn = AiReturn[0].tolist()
    playerIn = AiReturn.index(max(AiReturn))
    if board[playerIn] != 0:
        messagebox.showerror("Error", "Illegal move by AI")
        return
    board[playerIn] = player
    winner = check(board)
    turn += 1
    player *= -1
    update_board()
    if winner != 0 or turn == 10:
        end_game()

def end_game():
    if winner == 1:
        messagebox.showinfo("Game Over", "O won")
    elif winner == -1:
        messagebox.showinfo("Game Over", "X won")
    else:
        messagebox.showinfo("Game Over", "It's a tie")
    for button in buttons:
        button.config(state=tk.DISABLED)

def reset_game():
    global board, winner, player, turn, AiPlayer
    board = [0] * 9
    winner = 0
    player = 1
    turn = 1
    for button in buttons:
        button.config(state=tk.NORMAL)
    update_board()
    AiPlayer = None
    ask_ai_start()

def ask_ai_start():
    global AiPlayer
    AiPlayer = messagebox.askyesno("AI Start", "Should AI start?")
    if AiPlayer:
        AiPlayer = 1
        ai_move()
    else:
        AiPlayer = -1

# Initialize game variables
board = [0] * 9
winner = 0
player = 1
turn = 1

# Load the AI model
model = keras.models.load_model('model_tictactoe_tanh.keras')

# Initialize Tkinter GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

reset_button = tk.Button(root, text="Reset", font=('normal', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

ask_ai_start()

root.mainloop()
