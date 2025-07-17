# Username Validation System

## Description  
This Python script is a simple username validation system that repeatedly prompts the user to enter a username until the correct one ("Mary") is provided. It tracks the number of attempts made before successful validation.

## Features  
- **Input Validation**: Checks if the entered username matches "Mary"  
- **Attempt Counter**: Keeps track of how many tries the user makes  
- **Case-Sensitive Check**: Only "Mary" (exact match) is accepted  
- **Immediate Feedback**: Informs the user if the username is invalid  

## How It Works  
1. The program starts an infinite loop (`while True`)  
2. The user is prompted to enter a username  
3. The attempt counter (`attempts`) increments by 1 with each try  
4. If the username is "Mary":  
   - Prints a welcome message  
   - Displays the total number of attempts  
   - Exits the loop (`break`)  
5. If incorrect:  
   - Prints an error message  
   - Loops again  

## Usage  
```python
python username_validator.py