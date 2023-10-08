import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial bold"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(counter_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        window.attributes('-topmost', True)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        window.attributes('-topmost', True)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        window.attributes('-topmost', False)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(counter_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_section = math.floor(REPS / 2)
        for _ in range(work_section):
            mark += "✔️"
        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
window.iconbitmap('assets/tomato.ico')

title_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="assets/tomato.png")
canvas.create_image(100, 112, image=tomato_png)
counter_text = canvas.create_text(102, 130, text="00:00", fill="white",
                                  font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", command=start_timer, bg=GREEN, padx=5, pady=5)
start_button.grid(column=0, row=3)

reset_button = Button(text="RESET", command=reset, bg=PINK, padx=5, pady=5)
reset_button.grid(column=2, row=3)

tick_label = Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
tick_label.grid(column=1, row=4)

credit_label = Label(text="Developed by Shan Khalam", font=(FONT_NAME, 7), bg=YELLOW, fg=PINK)
credit_label.grid(column=1, row=5)
window.mainloop()
