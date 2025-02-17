# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:17:41 2024

@author: Siddhi Chaudhari
"""

import tkinter as tk
import time
import winsound
import threading

def display_current_time():
    while True:

        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d")
        label4.config(text=f"Current time: {current_time}\nCurrent date: {current_date}", font=('times', 12))
        time.sleep(1)

def check_alarm():
    
    while True:
        desired_time = hour_var.get() + ":" + minute_var.get()
        desired_date = month_var.get() + "-" + day_var.get()
        current_time = time.strftime("%H:%M")
        current_date = time.strftime("%m-%d")
        if current_time == desired_time and current_date==desired_date:
            comment = num1.get() # Get the comment entered by the user
            label2.config(text="Wake up! It's alarm time!", font=('times', 12))
            label3.config(text=f"Alarm Label: {comment}", font=('times', 12)) # Display the comment
            for i in range(3):
                winsound.Beep(1000, 700)
                time.sleep(0.1)
            button1 = tk.Button(window, text="Snooze", fg="white", bg="black", command=snooze_thread, font=('times', 12))
            button1.grid(row=6,column=2)
            break
        time.sleep(1)

def set_alarm():
    threading.Thread(target=check_alarm).start()

def snooze_thread():
    threading.Thread(target=snooze).start()
    
def snooze():
    desired_date = month_var.get() + "-" + day_var.get()
    desired_time = hour_var.get() + ":" + minute_var.get()
    hours, minutes = map(int, desired_time.split(":"))
    minutes += 1
    if minutes >= 60:
        hours += 1
        minutes = minutes % 60
    desired_time = str(hours).zfill(2) + ":" + str(minutes).zfill(2)
    while True:
        current_time = time.strftime("%H:%M")
        current_date = time.strftime("%m-%d")
        if current_time == desired_time and current_date==desired_date:
            comment = num1.get() # Get the comment entered by the user
            label2.config(text="Wake up! It's alarm time!", font=('times', 12))
            label3.config(text=f"Alarm Label: {comment}", font=('times', 12)) # Display the comment
            for i in range(3):
                winsound.Beep(1000, 700)
                time.sleep(0.1)
            break
        time.sleep(1)

# Create the main window
window = tk.Tk()
window.title("Alarm Clock")
window.configure(bg="#D6EAF8")
# Create dropdowns for hours and minutes
months=[str(a).zfill(2) for a in range(1,13)]
days=[str(b).zfill(2) for b in range(1,31)]
hours = [str(h).zfill(2) for h in range(24)] # Generate 2-digit hour strings
minutes = [str(m).zfill(2) for m in range(60)] # Generate 2-digit minute strings

hour_var = tk.StringVar(window)
hour_var.set("Hours") # Set default hour
hour_dropdown = tk.OptionMenu(window, hour_var, *hours)
hour_dropdown.grid(row=2, column=1)

minute_var = tk.StringVar(window)
minute_var.set("Minutes") # Set default minute
minute_dropdown = tk.OptionMenu(window, minute_var, *minutes)
minute_dropdown.grid(row=2, column=2)

month_var = tk.StringVar(window)
month_var.set("Month") # Set default minute
month_dropdown = tk.OptionMenu(window, month_var, *months)
month_dropdown.grid(row=2, column=3)

day_var = tk.StringVar(window)
day_var.set("Day") # Set default minute
day_dropdown = tk.OptionMenu(window, day_var, *days)
day_dropdown.grid(row=2, column=4)

# To display current time
label4 = tk.Label(window, text=" ", bg="#D6EAF8", font=('times', 12))
label4.grid(row=9, column=2)

label1 = tk.Label(window, text=" ", bg="#D6EAF8", font=('times', 13))
label1.grid(row=1, column=2)

label2 = tk.Label(window, text=" ", bg="#D6EAF8")
label2.grid(row=6, column=1)

label3 = tk.Label(window, text=" ", bg="#D6EAF8")
label3.grid(row=7, column=1)

l = tk.Label(window, text=" ", bg="#D6EAF8")
l.grid(row=4, column=1)

# create alarm label
l1 = tk.Label(window, text="Enter Alarm Label:", bg="#D6EAF8", font=('times', 11))
l1.grid(row=5, column=1)

# Create an entry for comment
num1 = tk.Entry(window, background="white", font=('times', 11))
num1.grid(row=5, column=2)

# Create the Set Alarm button
button = tk.Button(window, text="Set Alarm", fg="white", bg="black", command=set_alarm, font=('times', 12))
button.grid(row=2, column=5)


# Using multithreading
current_time_thread = threading.Thread(target=display_current_time)
current_time_thread.start()

window.mainloop()

#end