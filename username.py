#a simple username validation python script
attempts = 0
while True:
    username = input('Enter username: ')
    attempts += 1
    if username == 'Mary':
        print(f"Hello, Mary. Welcome! \nAttempts: {attempts}")
        break
    else:
        print(f"{username} is not a valid name. Try again.")
        
        
        



