#2nd commit
import tkinter as tk
import random

# Mapping dictionaries
dict_choices = {0: "snake", 1: "water", 2: "gun"}
rDict = {"snake": 0, "water": 1, "gun": 2}

# Scores
score1 = 0
score2 = 0

# Function to play game
def play(user_choice):
    global score1, score2
    robot = random.choice([0, 1, 2])  # Computer choice

    result_text = f"You chose {dict_choices[user_choice]}, Computer chose {dict_choices[robot]}.\n"

    if user_choice == robot:
        result_text += "It's a draw!"
    elif (user_choice == 0 and robot == 1) or \
         (user_choice == 1 and robot == 2) or \
         (user_choice == 2 and robot == 0):
        score1 += 1
        result_text += "🎉 You won this round!"
    else:
        score2 += 1
        result_text += "😢 You lost this round!"

    # Update labels
    scoreboard.config(text=f"Scoreboard:\nYou - {score1} | Computer - {score2}")
    result_label.config(text=result_text)

# Exit game
def end_game():
    if score1 > score2:
        final_result = f"🏆 You won by {score1 - score2} rounds!"
    elif score2 > score1:
        final_result = f"💀 You lost by {score2 - score1} rounds!"
    else:
        final_result = "⚖️ Overall Draw !!"
    result_label.config(text=final_result)

# GUI setup
root = tk.Tk()
root.title("Snake Water Gun Game")

# Heading
heading = tk.Label(root, text="🐍 Snake | 💧 Water | 🔫 Gun", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Scoreboard
scoreboard = tk.Label(root, text="Scoreboard:\nYou - 0 | Computer - 0", font=("Arial", 14))
scoreboard.pack(pady=10)

# Buttons for choices
frame = tk.Frame(root)
frame.pack(pady=10)

btn_snake = tk.Button(frame, text="Snake 🐍", width=12, command=lambda: play(0))
btn_snake.grid(row=0, column=0, padx=5)

btn_water = tk.Button(frame, text="Water 💧", width=12, command=lambda: play(1))
btn_water.grid(row=0, column=1, padx=5)

btn_gun = tk.Button(frame, text="Gun 🔫", width=12, command=lambda: play(2))
btn_gun.grid(row=0, column=2, padx=5)

# Result Label
result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=20)

# Exit Button
btn_exit = tk.Button(root, text="End Game", width=12, command=end_game, fg="red")
btn_exit.pack(pady=10)

# Run the app
root.mainloop()
