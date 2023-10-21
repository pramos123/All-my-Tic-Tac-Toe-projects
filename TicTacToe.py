from tkinter import *
import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X"
winner = None
gamerunning = True


#printing the game borad
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input 
def playerinput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Oops player is already in that spot!")



#check for win or tie 
def checkhorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkrow(board): 
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkdiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It is a Tie!")
        gamerunning = False

def checkwin():
    if checkhorizontle(board) or checkdiag(board) or checkrow(board):
        print(f"The winner is {winner}")

#switch player 

def switchplayer(): 
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

#computer 
def computer(board):
    while currentplayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchplayer()

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0], 
           [0,0,0],
           [0,0,0]]
label = Label(text= player + "turn", font=('consolas', 40))
label.pack(side="top")

window.mainloop()
#check for win or tie again 
while gamerunning: 
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)