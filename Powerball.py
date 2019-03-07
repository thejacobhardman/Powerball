# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 3/6/19
# Python Version 3.7.2

# Importing pkgs
import random
import os

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Tracks if the program is still running
Is_Running = True

# Tracks the user's input
User_Input = ""

# Checks if the user has guessed a valid number
Valid_Guess = False

# Stores the user's ticket guess
User_Ticket = []

# Stores the user's guess for the powerball
User_Powerball = 0

# Stores a random number
Random_Number = 0

# Stores the winning ticket numbers
Winning_Ticket = []

# Stores the winning powerball value
Winning_Powerball = 1

# Stores the number of correct numbers
Correct_Numbers = 0

########################################################### PROGRAM LOGIC ################################################################

### Generates the winning ticket and PowerBall
def Draw_Ticket():

    # Importing global variables
    global Valid_Guess
    global Random_Number
    global Winning_Ticket
    global Winning_Powerball

    i = 0
    while i < 3:
        Random_Number = random.randint(1,9)
        if Random_Number not in Winning_Ticket:
            Winning_Ticket.append(Random_Number)
            i += 1
        else:
            continue

    while Valid_Guess == False:
        Random_Number = random.randint(1,9)
        if Random_Number not in Winning_Ticket:
            Winning_Powerball = Random_Number
            break
        else:
            continue

### The player wants to guess their numbers manually
def Manual_Guess():

    # Importing global variables
    global User_Input
    global User_Ticket
    global User_Powerball

    # Debug statements

    # Clearing the screen to improve readability
    cls()

    print("You have chosen to guess your numbers manually.")
    print("Your guess must be between 1-9 and you cannot guess any number more than once with the exception of the powerball.\n")

    # Validating the user's first guess
    while Valid_Guess == False:
        User_Input = input("Please enter your first guess: ")
        if int(User_Input) >= 1 and int(User_Input) <= 9:
            User_Ticket.append(User_Input)
            break
        else:
            print("Please enter a valid guess.\n")

    # Validating the user's second guess
    while Valid_Guess == False:
        User_Input = input("Please enter your second guess: ")
        if User_Input not in User_Ticket and int(User_Input) >= 1 and int(User_Input) <= 9:
            User_Ticket.append(User_Input)
            break
        else:
            print("Please enter a valid guess.\n")

    # Validating the user's third guess
    while Valid_Guess == False:
        User_Input = input("Please enter your third guess: ")
        if User_Input not in User_Ticket and int(User_Input) >= 1 and int(User_Input) <= 9:
            User_Ticket.append(User_Input)
            break
        else:
            print("Please enter a valid guess.\n")

    # Validating the user's guess for the powerball
    while Valid_Guess == False:
        User_Input = input("Please enter your guess for the PowerBall: ")
        if int(User_Input) >= 1 and int(User_Input) <= 9:
            User_Powerball = int(User_Input)
            break
        else:
            print("Your PowerBall guess must be between 1 and 9.")

### The player wants to guess their numbers randomly
def Random_Guess():

    # Importing global variables
    global User_Input
    global User_Ticket
    global User_Powerball

    # Clearing the screen to improve readability
    cls()

    i = 0
    while i < 3:
        Random_Number = random.randint(1,9)
        if Random_Number not in User_Ticket:
            User_Ticket.append(Random_Number)
            i += 1
        else:
            continue

    while Valid_Guess == False:
        Random_Number = random.randint(1,9)
        if Random_Number not in User_Ticket:
            User_Powerball = Random_Number
            break
        else:
            continue

### Checks the player's guess (either manual or random) against the winning ticket
def Check_Result():

    # Importing global variables
    global User_Ticket
    global User_Powerball
    global Winning_Ticket
    global Winning_Powerball

    print("Your Ticket: ", end="")
    for Number in User_Ticket:
        print(Number, end=" ")
    print(User_Powerball)
    input("Press 'enter to continue.")

    print("The Drawing: ", end="")
    for Number in Winning_Ticket:
        print(Number, end=" ")
    print(Winning_Powerball)
    input("Press 'enter' to continue.")

### Calculates how much the user won based on the number of correct numbers
def Calculate_Winnings():

    # Importing global variables
    global User_Ticket
    global User_Powerball
    global Winning_Ticket
    global User_Powerball
    global Correct_Numbers


########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:
    print("Welcome to PowerBall!!!".center(100, " "))

    print("\nPlease enter '1' to select your numbers manually.")
    print("Please enter '2' to guess random numbers.")
    User_Input = input("\nPlease make a selection: ")

    if User_Input == "1":
        Draw_Ticket() # Generates the winning ticket and PowerBall
        Manual_Guess() # The player makes their guesses
        Check_Result() # Checks the player's guess against the winning ticket
    elif User_Input == "2":
        Draw_Ticket() # Generates the winning ticket and PowerBall
        Random_Guess() # The computer generates the player's random guess
        Check_Result() # Checks the player's guess against the winning ticket
    else:
        print("\nPlease enter a valid selection.")
        input("\nPress 'enter' to continue.")
        cls()