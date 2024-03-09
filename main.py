
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
def timer_reset():
    global reps
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    title_body.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_min)
        title_body.config(text="Long Break", fg=RED)
        check_mark.config(text="✔")

    elif reps % 2 == 0:
        count_down(short_break_min)
        title_body.config(text="Break", fg=PINK)
        check_mark.config(text="✔")


    else:
        count_down(work_min)
        title_body.config(text="Work", fg=GREEN)
        check_mark.config(text="")

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_body = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, ""))
title_body.grid(row=0, column=1)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command = timer_reset)
reset_button.grid(row=2, column=2)

window.mainloop()