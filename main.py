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

score = 0

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
    
    global score
    score = 0
    
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
    


# Check if x button is clicked or not
x_button_clicked = False

'''
Function to draw the game UI.
'''
def draw_game_window():
    
    global x_button_clicked
    
    '''
    Initialize timer object for questions
    EASY mode -> 60 seconds
    MEDIUM mode -> 45 seconds
    HARD mode -> 30 seconds
    '''
    if difficulty == "easy":
        question_timer = Timer(60)
    elif difficulty == "medium":
        question_timer = Timer(45)
    elif difficulty == "hard":
        question_timer = Timer(30)
    
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
    The message shows for three seconds and then the next question is shown.
    '''
    def check_answer(choice):
        
        global score
        
        # tells the timer to stop running
        answer_clicked.set()
        
        # A new timer for counting the wait time
        wait_timer = Timer(3)
        
        # tells that the wait time is over
        wait_time_over = threading.Event()
        
        wait_time_over.clear()
        
        if choice == "":
            message = f"The correct answer is {answers[correct_choice]}."
        elif choice == answers[correct_choice]:
            message = "Good Job!"
            if difficulty == "easy":
                score += 5
            elif difficulty == "medium":
                score += 10
            elif difficulty == "hard":
                score += 15
        elif choice != answers[correct_choice]:
            message = f"Not Quite. The correct answer is {answers[correct_choice]}."
        
        '''
        helper function to show the answer evaluation dialogue.
        Shows the dialogue for three seconds, and then the game_screen frame
        is destroyed. The next question is displayed.
        Displays the correct answer when timer runs out.
        '''
        def show_answer():
            
            # Only destroy elements from frame that exists
            if game_screen.winfo_exists():
                for item in game_screen.winfo_children():
                    item.destroy()
                    
            # Runs for exactly three seconds
            while wait_timer.get_time() > 0 and not wait_time_over.is_set() and not x_button_clicked:
                
                if x_button_clicked:
                    return

                # Draw message on frame that exists
                if game_screen.winfo_exists():
                    
                    message_label = tk.Label(
                        game_screen,
                        text = message,
                        font = SUBTITLE_FONT
                    )
                    labels["message_label"] = message_label
                    labels["message_label"].pack()
                
                # Decrements the timer
                wait_timer.count_down()
                time.sleep(1)
                
                '''
                to give the illusion of the label being shown for three seconds, the message_label
                is deleted and redrawn every second.
                '''
                labels["message_label"].destroy()
            
            # ends the wait time
            wait_time_over.set()
            
            # destroys the frame
            game_screen.destroy()
            
            if not game_screen.winfo_exists():
                # draws the next question
                draw_game_window()
        
        '''
        used to stop further execution if x-button is clicked,
        where the succeeding code is not needed.
        '''
        if x_button_clicked:
            return
        
        # creates and runs the showing dialogue thread.
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
            if x_button_clicked:
                return
            update_timer_label(question_timer.get_time())
            question_timer.count_down()
            time.sleep(1)
            
        if x_button_clicked:
            question_timer.reset()
            
        '''
        makes sure the correct answer is shown when timer runs out.
        '''
        if not answer_clicked.is_set():
            check_answer("")
            
    
    '''
    creates a random question tuple and unpacks it into three
    variables.
    '''
    question_set = Question()
    
    '''
    interchanges between types of questions on a 50-50 basis.
    '''
    seed = random.randint(0,100)
    if seed <= 50:
        question_set.change_question_type(0)
    else:
        question_set.change_question_type(1)
    
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
    
    score_label = tk.Label(
        game_screen,
        text = f"Score: {score}",
        font = PARAGRAPH_FONT
    )
    labels["score_label"] = score_label
    labels["score_label"].pack()
    
    if x_button_clicked:
        return
    
    '''
    Timer thread to run the timer separate from the main program.
    This allows the user to click the buttons while the timer runs
    "in the background."
    '''
    timer_thread = threading.Thread(target=update_time)
    
    # Starts the timer
    timer_thread.start()

'''
this function runs when x-button on top right is clicked.
the x_button_clicked variable is set to True, ending all the timer
threads.
Then the game window is destroyed.
'''       
def on_x_button_click():

   global x_button_clicked
   
   x_button_clicked = True
   
   game_window.destroy()
 
# Starts the game by drawing the home screen 
draw_home_screen()

# Listens for the x-button click event
game_window.protocol("WM_DELETE_WINDOW",on_x_button_click)

# Listens for any events
game_window.mainloop()

