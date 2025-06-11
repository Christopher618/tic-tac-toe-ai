from tkinter import *
from tkinter import font as tkFont
import logic

root = Tk()
root.geometry("400x400")
root.title("Tic-tac-toe AI")
root.iconbitmap("tic_tac_toe_ai/icons8-tic-tac-toe-32.ico")
root.config(bg="#0F0F0F")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(2, weight=1)

ft = tkFont.Font(family="Orbitron", size=14)
ft2 = tkFont.Font(family="Orbitron", size=10)

fr = Frame(root)
fr.grid(row=1, column=1)
for i in range(3):
    fr.grid_columnconfigure(i, weight=1)
    fr.grid_rowconfigure(i, weight=1)

message = Label(root, text="X - O", fg="white", bg="#0F0F0F" , font=ft)
message.grid(row=0, column=1)
play_again = Button(root, text="Play-again", width=10, height=2, command=lambda: again(), fg="white", bg="#FF1493", activebackground="#ff66cc", activeforeground="white", font=ft2)
play_again.grid(row=2, column=1)

gui_board = logic.initial_state()
button = [[None for _ in range(3)] for _ in range(3)]
for i, row in enumerate(button):
    for j, col in enumerate(row):
        btn = Button(fr, text="", padx=30, pady=25, command=lambda r=i, c=j: click_handling(r, c), fg="white", disabledforeground="white" ,bg="#FF1493", activebackground="#ff66cc", activeforeground="white", font=ft)
        btn.grid(row=i, column=j, sticky="nsew")
        button[i][j] = btn

def click_handling(r, c):
    global gui_board, message
    letter = logic.player(gui_board)
    message["text"] = "O-turns"
    if gui_board[r][c] is not None:
        return
    if letter == "X":
        button[r][c]["text"] = letter
        button[r][c]["state"] = DISABLED 
        gui_board = logic.result(gui_board, (r, c))
        if logic.terminal(gui_board):
            winner = logic.winner(gui_board)
            message["text"] = f"{winner} wins!!!" if winner else "It's a tie"
            for row in button:
                for cell in row:
                    cell["state"] = DISABLED
            return
        root.after(100, lambda: ai_turn())

def ai_turn():
    global gui_board, message

    letter = logic.player(gui_board)
    message["text"] = "X-turns"
    minimax = logic.minimax(gui_board)
    if minimax is None:
        return 
    a, b = minimax
    if button[a][b]["state"] is not DISABLED:
        button[a][b]["text"] = letter
        button[a][b]["state"] = DISABLED
        gui_board = logic.result(gui_board, (a, b))
        if logic.terminal(gui_board):
            winner = logic.winner(gui_board)
            message["text"] = f"{winner} wins!!!" if winner else "It's a tie"
            for row in button:
                for cell in row:
                    cell["state"] = DISABLED

def again():
    global gui_board
    
    if all(btn["state"] == DISABLED for row in button for btn in row):
        gui_board = logic.initial_state()

        for row in button:
            for btn in row:
                btn["text"] = ""
                btn["state"] = NORMAL
        message["text"] = "X - O"
       
root.mainloop()
