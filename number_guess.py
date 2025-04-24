import random
import tkinter as tk
from tkinter import messagebox

# Create main window    
root = tk.Tk()
root.title("Number Guesser")
root.configure(bg="#f0f8ff")

# Set to fullscreen
root.attributes('-fullscreen', True)
root.update()  # Ensure the window dimensions are updated

# Game variables
secret_number = random.randint(1, 100)
attempts = 0
game_active = True
best_score = float('inf')  # Track best score (lowest attempts)

# Create a canvas for gradient background
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Create a gradient background (light blue to white)
def create_gradient():
    height = root.winfo_screenheight()
    for i in range(height):
        r = int(240 - (i / height) * 40)  # Transition from #e0f2fe to #ffffff
        g = int(248 - (i / height) * 8)
        b = int(255 - (i / height) * 1)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, root.winfo_screenwidth(), i, fill=color)

create_gradient()

# Create and place widgets using grid
# Set a larger size for the shadow and main frame to ensure all widgets are visible
shadow_frame = tk.Frame(root, bg="#d1d5db")
shadow_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)

main_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="raised")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=380, height=480)

# Ensure main_frame is on top
main_frame.lift()

# Add widgets with centered text and padding
title = tk.Label(main_frame, text="Guess the Number", font=("Arial", 20, "bold"), bg="#ffffff", fg="#1e3a8a", anchor="center")
title.grid(row=0, column=0, pady=20, padx=20)  # Add padx for left/right margin

instructions = tk.Label(main_frame, text="I'm thinking of a number between 1 and 100", 
                       bg="#ffffff", fg="#374151", font=("Arial", 12), anchor="center")
instructions.grid(row=1, column=0, pady=10, padx=20)

entry = tk.Entry(main_frame, font=("Arial", 14), width=10, justify="center", bg="#e0f2fe", fg="#1e3a8a")
entry.grid(row=2, column=0, pady=20, padx=20)
entry.focus()

feedback = tk.Label(main_frame, text="", bg="#ffffff", font=("Arial", 12), anchor="center")
feedback.grid(row=3, column=0, pady=10, padx=20)

counter = tk.Label(main_frame, text="Attempts: 0", bg="#ffffff", fg="#374151", font=("Arial", 12), anchor="center")
counter.grid(row=4, column=0, pady=10, padx=20)

best_score_label = tk.Label(main_frame, text="Best Score: --", bg="#ffffff", fg="#374151", font=("Arial", 12), anchor="center")
best_score_label.grid(row=5, column=0, pady=10, padx=20)

# Button click handlers
def update_submit_button_state(*args):
    try:
        guess = entry.get()
        if guess.strip() == "" or not (1 <= int(guess) <= 100):
            submit.config(state="disabled")
        else:
            submit.config(state="normal")
    except ValueError:
        submit.config(state="disabled")

def handle_buttons(button_type):
    global attempts, game_active, secret_number, best_score
    
    if button_type == "submit":
        if not game_active:
            return
            
        try:
            guess = int(entry.get())
            attempts += 1
            counter.config(text=f"Attempts: {attempts}")
            
            if guess < 1 or guess > 100:
                feedback.config(text="Please enter 1-100!", fg="#dc2626")
            elif guess < secret_number:
                feedback.config(text="Too low! Try higher.", fg="#1e40af")
            elif guess > secret_number:
                feedback.config(text="Too high! Try lower.", fg="#1e40af")
            else:
                feedback.config(text="Congratulations! You won!", fg="#16a34a")
                game_active = False
                best_score = min(best_score, attempts)
                best_score_label.config(text=f"Best Score: {best_score}")
                messagebox.showinfo("Winner!", f"You won in {attempts} tries!\nClick OK to play again.")
                handle_buttons("new")  # Auto-restart game
                
            entry.delete(0, tk.END)
        except ValueError:
            feedback.config(text="Numbers only please!", fg="#dc2626")
            
    elif button_type == "new":
        secret_number = random.randint(1, 100)
        attempts = 0
        game_active = True
        counter.config(text="Attempts: 0")
        feedback.config(text="")
        entry.delete(0, tk.END)
        entry.focus()

# Button hover effects
def on_enter(e, button):
    button.config(bg="#2563eb")

def on_leave(e, button):
    button.config(bg="#3b82f6")

# Create buttons
button_frame = tk.Frame(main_frame, bg="#ffffff")
button_frame.grid(row=6, column=0, pady=20, padx=20)

submit = tk.Button(button_frame, text="Submit Guess", 
                  command=lambda: handle_buttons("submit"), bg="#3b82f6", fg="#ffffff", font=("Arial", 10, "bold"), padx=10, pady=5, state="disabled")
submit.pack(side=tk.LEFT, padx=10)
submit.bind("<Enter>", lambda e: on_enter(e, submit))
submit.bind("<Leave>", lambda e: on_leave(e, submit))

new_game = tk.Button(button_frame, text="New Game", 
                    command=lambda: handle_buttons("new"), bg="#3b82f6", fg="#ffffff", font=("Arial", 10, "bold"), padx=10, pady=5)
new_game.pack(side=tk.LEFT, padx=10)
new_game.bind("<Enter>", lambda e: on_enter(e, new_game))
new_game.bind("<Leave>", lambda e: on_leave(e, new_game))

# Bind entry to update submit button state
entry.bind("<KeyRelease>", update_submit_button_state)

# Keyboard support
root.bind('<Return>', lambda e: handle_buttons("submit") if submit.cget("state") == "normal" else None)

# Exit fullscreen on Esc key
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

# Start the game
root.mainloop()