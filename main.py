import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from CONSTANTS import *

difficulties = ["easy","medium","hard"]

game_window = tk.Tk()

game_window.minsize(WIDTH,HEIGHT)

TITLE_FONT = tkFont.Font(family="Times New Roman",size=30)
SUBTITLE_FONT = tkFont.Font(family="Verdana",size=20)

welcome_banner = tk.Label(
    text="Test your U.S. geography skills here!",
    font=TITLE_FONT
)
welcome_banner.pack()

option_dialogue = tk.Label(
    text="Please select a difficulty:",
    font=SUBTITLE_FONT
)
option_dialogue.pack()

option_menu = ttk.Combobox(game_window, values=difficulties)
option_menu.set("Select a difficulty:")
option_menu.pack()

game_window.mainloop()