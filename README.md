*🎮 Number Guessing Game*

This is a simple Python console game where the user tries to guess a randomly generated number between 1 and 10.
📋 How It Works

    Start the Game

        The game picks a random number between 1 and 10.

    Make a Guess

        The player enters their guess.

    Check the Guess

        If the guess is correct, the game congratulates the player.

        If the guess is wrong, the player is asked to guess again.

        The game adds a penalty to the accuracy score for each wrong attempt.

    Invalid Input Check

        If the player enters a number greater than 10 during retry, the inner loop breaks and moves on.

    Accuracy Score

        Accuracy starts at 100%.

        Each wrong guess reduces accuracy by 10%.

    Play Again

        After finishing, the player can choose to play again by entering play.

✅ Features

    Random secret number generation.

    Loop until correct guess or invalid input.

    Accuracy score that decreases with each wrong attempt.

    Option to replay the game.

🐍 How to Run

    Make sure you have Python installed.

    Copy the code into a file, e.g., guessing_game.py.

    Run it using:

    python guessing_game.py

⚠️ Notes

    If the player enters a number greater than 10 during a retry, the loop exits early.

Enjoy guessing! 🎉
