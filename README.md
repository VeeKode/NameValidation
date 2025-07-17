# NameValidation
Description
This Python script is a simple username validation system that repeatedly prompts the user to enter a username until the correct one ("Mary") is provided. It tracks the number of attempts made before successful validation.

Features
Input Validation: Checks if the entered username matches "Mary".
Attempt Counter: Keeps track of how many tries the user makes.
Case-Sensitive Check: Only "Mary" (exact match) is accepted.
Immediate Feedback: Informs the user if the username is invalid.

How It Works
The program starts a loop that runs indefinitely (while True).
The user is prompted to enter a username.
The attempt counter (attempts) increments by 1 with each try.
If the username is "Mary", the program:
Prints a welcome message.
Displays the total number of attempts.
Exits the loop (break).
If the username is incorrect, it prints an error message and loops again.