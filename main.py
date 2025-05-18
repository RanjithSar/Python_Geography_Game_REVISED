import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

import random

from CONSTANTS import *
from question import Question

'''
function to quit tkinter. Used in the 
quit button.
'''
def close_application():
    game_window.destroy()
    
'''
Stores the pre-defined difficulty levels and the 
game modes for easy access throughout the program.
'''
difficulties = ["easy","medium","hard"]
difficulty = ""
game_modes = ["home screen","game play"]
current_mode = game_modes[0]

'''
The main window the game takes place in.
WIDTH and HEIGHT are found in CONSTANTS.py file
in root directory.
'''
game_window = tk.Tk()
game_window.minsize(WIDTH,HEIGHT)

'''
defined fonts for asthetics of game.
'''
TITLE_FONT = tkFont.Font(family="Times New Roman",size=30)
SUBTITLE_FONT = tkFont.Font(family="Verdana",size=20)

'''
Draws the main menu. The program always starts here on startup.
'''
def draw_home_screen():
    
    '''
    This function switches from home screen state to gameplay state,
    effectively starting the game.
    It removes everything from the home screen and then calls the draw_game_window
    method to draw the game UI.
    '''
    def switch_states():
        global difficulty, current_mode
        difficulty = option_menu.get()
        if "Select a difficulty:" not in difficulty:
            for item in start_screen.winfo_children():
                item.destroy()
            start_screen.destroy()
            current_mode = game_modes[1]
            draw_game_window()

    '''
    The frame holding all the home screen elements.
    '''
    start_screen = tk.Frame(
        game_window,
        width=WIDTH,
        height=HEIGHT
    )
    start_screen.pack()

    welcome_banner = tk.Label(
        start_screen,
        text="Test your U.S. geography skills here!",
        font=TITLE_FONT
    )
    welcome_banner.pack()

    option_dialogue = tk.Label(
        start_screen,
        text="Please select a difficulty:",
        font=SUBTITLE_FONT
    )
    option_dialogue.pack()

    option_menu = ttk.Combobox(start_screen, values=difficulties)
    option_menu.set("Select a difficulty:")
    option_menu.pack()

    submit_button = tk.Button(start_screen, text="Start", command=switch_states)
    submit_button.pack()

    quit_button = tk.Button(start_screen, text="Quit", command=close_application)
    quit_button.pack()
    
'''
Function to draw the game UI.
'''
def draw_game_window():
    
    game_screen = tk.Frame(
        game_window,
        width=WIDTH,
        height=HEIGHT
    )
    game_screen.pack()
    

    current_question = Question()
    
    seed = random.randint(0,100)
    if seed < 50:
        current_question.change_question_type(0)
    else:
        current_question.change_question_type(1)
    
    question, answers, correct_choice = current_question.generate_question()
    
    display = tk.Label(
        game_screen,
        text=question
    )
    display.pack()
    
    for i in range(4):
        ans = tk.Button(
            game_screen,
            text=answers[i]
        )
        ans.pack()
    
'''
starts the program on home page.
'''
draw_home_screen()

# Listens for any events
game_window.mainloop()