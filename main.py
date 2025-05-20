import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

import random
import threading
import time

from CONSTANTS import *
from question import Question
from timer import Timer

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
PARAGRAPH_FONT = tkFont.Font(family="Verdana",size=15)

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
    
    
# Initialize timer object for questions
question_timer = Timer(60)


# Check if x button is clicked or not
x_button_clicked = False

'''
Function to draw the game UI.
'''
def draw_game_window():
    
    global x_button_clicked
    
    question_timer.reset()
    
    '''
    checks if an answer choice is pressed.
    This event is set when an answer choice is pressed.
    '''
    answer_clicked = threading.Event()
    
    '''
    game screen frame to hold all widgets
    '''
    game_screen = tk.Frame(
        game_window,
        width = WIDTH,
        height = HEIGHT
    )
    game_screen.pack()
    
    # Stores all labels displayed on the screen
    labels = {}
    
    '''
    helper function for buttons to check the answer.
    It first sets the answer_choice event and then 
    clears everything within the frame. Then, it
    displays a message based on whether the answer is correct or
    not.
    '''
    def check_answer(choice):
        
        answer_clicked.set()
        
        wait_timer = Timer(3)
        wait_time_over = threading.Event()
        
        def show_answer():
            
            if game_screen.winfo_exists():
                for item in game_screen.winfo_children():
                    item.destroy()
            
            while wait_timer.get_time() > 0 and not wait_time_over.is_set():
        
                if choice == answers[correct_choice]:
                    message = "Good Job!"
                else:
                    message = f"Not Quite. The correct answer is {answers[correct_choice]}."
                    
                if game_screen.winfo_exists():
                    
                    message_label = tk.Label(
                        game_screen,
                        text = message,
                        font = SUBTITLE_FONT
                    )
                    labels["message_label"] = message_label
                    labels["message_label"].pack()

                wait_timer.count_down()
                time.sleep(1)
                
                labels["message_label"].destroy()
                
            wait_time_over.set()
            
            game_screen.destroy()
            
            draw_game_window()
        
        timer_thread = threading.Thread(target = show_answer)
        
        timer_thread.start()
        
    
    '''
    helper function to update just the timer label.
    Accesses this specific label from the labels dicitionary.
    '''
    def update_timer_label(time_left):
        labels["timer_label"].config(text=f"Time left: {time_left} seconds.")
    
    '''
    helper function for timer thread to count down the timer
    and update the label accordingly using the update_timer_label function.
    the timer runs until it runs out or an answer choice is clicked.
    '''
    def update_time():
        while question_timer.get_time() >= 0 and not answer_clicked.is_set():
            update_timer_label(question_timer.get_time())
            question_timer.count_down()
            time.sleep(1)
            
    
    '''
    creates a random question tuple and unpacks it into three
    variables.
    '''
    question_set = Question()
    question, answers, correct_choice = question_set.generate_question()
    
    '''
    shows the question on the game window as a label.
    '''
    question_label = tk.Label(
        game_screen,
        text = question,
        font = SUBTITLE_FONT
    )
    labels["question_label"] = question_label
    labels["question_label"].pack()
    
    '''
    creates four answer buttons displaying the possible answers.
    when clicked, each button will check the answer using its given
    answer choice from the answers list passed as the argument to the 
    check_answer function.
    '''
    for i in range(4):
        ans_button = tk.Button(
            game_screen,
            text = answers[i],
            width = 10,
            height = 3,
            command = lambda choice=answers[i]: check_answer(choice)
        )
        ans_button.pack()
     
    '''
    Displays the empty timer label, which is then updated by the 
    timer thread.
    '''
    timer_label = tk.Label(
        game_screen,
        text = "",
        font = PARAGRAPH_FONT
    )
    labels["timer_label"] = timer_label
    labels["timer_label"].pack()
    
    '''
    Timer thread to run the timer separate from the main program.
    This allows the user to click the buttons while the timer runs
    "in the background."
    '''
    timer_thread = threading.Thread(target=update_time)
    
    # Starts the timer
    timer_thread.start()
        
        
    
draw_home_screen()

# Listens for any events
game_window.mainloop()

