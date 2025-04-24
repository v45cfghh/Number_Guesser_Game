*Number Guesser Game*
Overview
The Number Guesser Game is a fun, interactive GUI-based game built using Python and the Tkinter library. Players attempt to guess a randomly generated number between 1 and 100, receiving real-time feedback on whether their guess is too high, too low, or correct. The game tracks the number of attempts and maintains the best score (lowest number of attempts). It features a visually appealing gradient background, hover effects on buttons, and keyboard support for an enhanced user experience.
Features

Interactive GUI: Built with Tkinter, featuring a clean and modern interface.
Random Number Generation: A secret number between 1 and 100 is generated for each game.
Real-Time Feedback: Displays messages indicating if the guess is too high, too low, or correct.
Attempt Counter: Tracks the number of guesses made in the current game.
Best Score Tracking: Records the lowest number of attempts across games.
Input Validation: Ensures guesses are valid numbers between 1 and 100.
Visual Enhancements: Gradient background, button hover effects, and a shadow frame for a polished look.
Keyboard Support: Press Enter to submit a guess and Escape to exit fullscreen mode.
Responsive Design: Fullscreen mode with centered widgets for a consistent experience.

Installation
To run the Number Guesser Game on your local machine, follow these steps:
Prerequisites

Python 3.x installed (Python 3.6 or higher recommended).
Tkinter (usually included with Python; if not, install it via your package manager).

Steps

Clone the Repository (if hosted on GitHub):git clone https://github.com/v45cfghh/Number_Guesser_Game/tree/main
cd number-guesser-game


Ensure Dependencies:Tkinter is part of Python's standard library. Verify it’s available by running:python -m tkinter

If Tkinter is missing, install it (e.g., on Ubuntu):sudo apt-get install python3-tk


Run the Game:python number_guesser.py



Usage

Launch the game by running the script (python number_guesser.py).
The game opens in fullscreen mode with a centered interface.
Enter a number between 1 and 100 in the input field.
Click Submit Guess or press Enter to check your guess.
Receive feedback:
"Too low! Try higher." or "Too high! Try lower."
"Congratulations! You won!" upon guessing correctly.


Click New Game to start a new round or continue after winning.
Press Escape to exit fullscreen mode.
The game tracks your attempts and displays your best score.

Code Structure

Main File: number_guesser.py
Initializes the Tkinter window and game variables.
Creates a gradient background using a canvas.
Manages the game logic, user input, and UI updates.


Key Functions:
create_gradient(): Generates the gradient background.
update_submit_button_state(): Enables/disables the submit button based on input.
handle_buttons(): Handles submit and new game actions.



Learning Outcomes
Through this project, I gained experience in:

Designing and implementing a GUI with Tkinter.
Managing game logic and state in Python.
Enhancing UI/UX with visual effects (gradients, hover effects).
Implementing input validation and error handling.
Adding keyboard support for improved accessibility.

Credits

Developer: Vivek 
Mentor: Special thanks to Saurav Sir for guidance and support throughout the project.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Feel free to fork this repository, submit issues, or create pull requests with improvements or additional features!
