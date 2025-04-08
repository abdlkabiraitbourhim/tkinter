
import tkinter as tk
import time
import random

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)

def convert_temperature():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_label.config(text=f"{fahrenheit}°F")

def button_clicked():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    button.config(bg=random.choice(["red", "green", "blue"]))

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("Arial", 50))
clock_label.pack()

update_time()

celsius_label = tk.Label(root, text="Celsius:")
celsius_label.pack()

celsius_entry = tk.Entry(root)
celsius_entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

fahrenheit_label = tk.Label(root, text="")
fahrenheit_label.pack()

score = 0
score_label = tk.Label(root, text="Score: 0")
score_label.pack()

button = tk.Button(root, text="Click Here", command=button_clicked)
button.pack()

root.mainloop()