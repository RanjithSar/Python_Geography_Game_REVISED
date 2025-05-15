import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from CONSTANTS import *

def close_application():
    game_window.destroy()
    
difficulties = ["easy","medium","hard"]
difficulty = ""
game_modes = ["home screen","game play"]
current_mode = game_modes[0]

game_window = tk.Tk()

game_window.minsize(WIDTH,HEIGHT)

TITLE_FONT = tkFont.Font(family="Times New Roman",size=30)
SUBTITLE_FONT = tkFont.Font(family="Verdana",size=20)

def draw_home_screen():
    
    def get_difficulty():
        global difficulty, current_mode
        difficulty = option_menu.get()
        switch_states()
        
    def switch_states():
        for item in start_screen.winfo_children():
            item.destroy()
        current_mode = game_modes[1]
        draw_game_window()
        #print(difficulty)

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

    submit_button = tk.Button(start_screen, text="Start", command=get_difficulty)
    submit_button.pack()

    quit_button = tk.Button(start_screen, text="Quit", command=close_application)
    quit_button.pack()
    
def draw_game_window():
    game_screen = tk.Frame(
        game_window,
        width=WIDTH,
        height=HEIGHT
    )
    game_screen.pack()
    
    display = tk.Label(
        game_screen,
        text=f"You selected {difficulty} mode!"
    )
    display.pack()
    
draw_home_screen()

game_window.mainloop()