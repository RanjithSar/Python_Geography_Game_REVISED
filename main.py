import tkinter as tk
import tkinter.font as tkFont
from CONSTANTS import *

game_window = tk.Tk()

game_window.minsize(WIDTH,HEIGHT)

TITLE_FONT = tkFont.Font(family="Times New Roman",size=30)

welcome_banner = tk.Label(
    text="Test your U.S. geography skills here!",
    font=TITLE_FONT
)
welcome_banner.pack()

game_window.mainloop()