#this file was created by: Zydaan Khan

'''
Goals:
Create a window
create a 3 by 3 grid in the window 
add things in the grid
integrate player 2
add music
clean up some messes
'''

from tkinter import *
import random
import pygame

# initialize the sound mixer module
pygame.mixer.init()
# load a music file
pygame.mixer.music.load(('Elevator_Music.mp3'))
# set the volume level for the currently loaded music
pygame.mixer.music.set_volume(0.4)
# amount of times the music plays
pygame.mixer.music.play(loops=-1)

# defines next turn with parameters row and column
# the whole block manages the turn-based gameplay, updates the button text, changes the player, and updates the label text based on the game's state (win, tie, or ongoing)
def next_turn(row, column):
    # used to declare variable player
    global player
    # checks the if the players a winner based on the allignment of the buttons
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # checks if the value of the player variable is equal to the value of players[0], indicating that it is the first player's turn
        if player == players[0]:
            # update the text displayed on a button
            buttons[row][column]['text'] = player
            # conditional statement that checks if the player won or not
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            # indicates that the first player has won the game and updates the label's text to display a message indicating the first player's victory.
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            # indicates that the game has resulted in a tie and updates the label's text to display a message indicating a tie or draw in the game.
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        # if the other ifs don't apply
        # this whole block updates the label's text accordingly based on whether the game is ongoing, a player has won, or the game has ended in a tie
        else:
            #  updates the text displayed on a specific button
            buttons[row][column]['text'] = player
            #  when there is no winner yet in the game it updates the player variable to indicate that it is now the turn of the first player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
            # indicates that the second player has won the game
            elif check_winner() is True:
                # updates the label's text to display a message indicating the second players victory in the game
                label.config(text=(players[1]+" wins"))
            # indicates that the game has resulted in a tie
            elif check_winner() == "Tie":
                # updates the label's text to display a message indicating a tie or draw in the game.
                label.config(text="Tie!")

# defines check_winner
def check_winner():
    # describes the row and manipulates it
    for row in range(3):
        # this block checks if the text values of the buttons in a specific row are equal and not empty and if they are, it highlights the buttons by changing their background color to green and returns True to indicate a winning condition
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    # describes the row and manipulates it
    for column in range(3):
        # this block checks if the text values of the buttons in a specific row are equal and not empty and if they are, it highlights the buttons by changing their background color to green and returns True to indicate a winning condition
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    # this block checks if the text values of the buttons in a specific row are equal and not empty and if they are, it highlights the buttons by changing their background color to green and returns True to indicate a winning condition
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    # checks if the text values of the buttons in a diagonal line from the top right to the bottom left are equal and not empty.
    # Highlites green based off True or False.
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    # executed when there are no empty spaces left on the game board and updates the background color of all buttons to yellow and returns the string "Tie"
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    # if not a tie, ignore and keep the game going
    else:
        return False

# this block determines if there are any empty spaces remaining on the game board by counting the buttons and counting the number of empty spaces.
def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

# resets the game state by clearing the text on all buttons and setting the background color to a light gray
# also randomly determines the starting player and updates the label to display the current player's turn
def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

# creates a window
window = Tk()
# titles the window "Tic-Tac-Toe"
window.title("Tic-Tac-Toe")
# gives player 1 and 2 variables for the game board and title for the turn
players = ["x","o"]
# randomizes the players starting turn
player = random.choice(players)
# formats the buttons in a 3 by 3 structure
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# displays the text indicating the current player's turn
label = Label(text=player + " turn", font=('consolas',40))
# moves the label to the top
label.pack(side="top")

# when clicked, restarts the game
reset_button = Button(text="restart", font=('consolas',20), command=new_game)
# moves the reset button to the top of the window
reset_button.pack(side="top")

# creates a frame widget
frame = Frame(window)
# packs it onto the main window using the default packing options
frame.pack()

for row in range(3):
    # commands where every button goes and what column
    # how big the buttons are
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

# keeps the application running until it is closed or terminated by the user
window.mainloop()   