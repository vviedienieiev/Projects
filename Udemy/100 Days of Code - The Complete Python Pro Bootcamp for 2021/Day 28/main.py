import tkinter
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
SEC_IN_MIN = 60
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global REPS

    window.after_cancel(TIMER)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * SEC_IN_MIN
    short_break_sec = SHORT_BREAK_MIN * SEC_IN_MIN
    long_break_sec = LONG_BREAK_MIN * SEC_IN_MIN

    if REPS%8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif REPS%2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global TIMER

    count_min = math.floor(count/SEC_IN_MIN)
    count_sec = count % SEC_IN_MIN
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count-1)
    else:
        start_time()
        check_marks.config(text="✓"*math.floor(REPS/2))



# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(row=0,column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=False, command=start_time)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=False, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME,14,"bold"))
check_marks.grid(row=3, column=1)

window.mainloop()