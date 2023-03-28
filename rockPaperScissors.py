#------------- EXTERNAL LIBRARIES -------------#
import random

#------------- FUNCTIONS -------------#

def playGame():
    print("To play, enter 'r' for 'rock', 'p' for 'paper', and 's' for 'scissors'.")
    userWeapon = input("Make your choice: ")
    print("\n")
    userWeapon = userWeapon.lower()
    
    computerChoice = random.randint(1, 3)
    computerWeapon = ""

    match computerChoice:
        case 1:
            computerWeapon = "r"
        case 2:
            computerWeapon = "p"
        case 3:
            computerWeapon = "s"
        case _:
            print("What?!? How did this happen?!?")

    if userWeapon == computerWeapon:
        match userWeapon:
            case "r":
                print("Draw! You and the Computer chose the same weapon: Rock\n")
            case "p":
                print("Draw! You and the Computer chose the same weapon: Paper\n")
            case "s":
                print("Draw! You and the Computer chose the same weapon: Scissors\n")
            case _:
                print("This should not be happening.")    
    elif userWeapon == "r" and computerWeapon == "p":
        print("Your Weapon: Rock")
        print("Computer's Weapon: Paper")
        print("Paper beats Rock. The Computer wins!\n")
    elif userWeapon == "r" and computerWeapon == "s":
        print("Your Weapon: Rock")
        print("Computer's Weapon: Scissors")
        print("Rock beats Scissors. You win!\n")
    elif userWeapon == "p" and computerWeapon == "r":
        print("Your Weapon: Paper")
        print("Computer's Weapon: Rock")
        print("Paper beats Rock. You win!\n")
    elif userWeapon == "p" and computerWeapon == "s":
        print("Your Weapon: Paper")
        print("Computer's Weapon: Scissors")
        print("Scissors beats Paper. The Computer wins!\n")
    elif userWeapon == "s" and computerWeapon == "r":
        print("Your Weapon: Scissors")
        print("Computer's Weapon: Rock")
        print("Rock beats Scissors. The Computer wins!\n")
    elif userWeapon == "s" and computerWeapon == "p":
        print("Your Weapon: Scissors")
        print("Computer's Weapon: Paper")
        print("Scissors beats Paper. You win!\n")
    else:
        print("I don't know how we got here, but we did. ")
    
    playAgainOption()
    

def playAgainOption():
    userPlayAgainChoice = input("Play again? 'Y' for 'Yes' or 'N' for 'No': ")
    print("\n")
    userPlayAgainChoice = userPlayAgainChoice.upper()

    match userPlayAgainChoice:
        case "Y":
            playGame()
        case "N":
            print("Thank for playing!")
        case _:
            print("Invalid input. Try again.\n")
            playAgainOption()


#------------- MAIN -------------#
print("ROCK, PAPER, SCISSORS!!!")

print("* * * * * MENU * * * * *")
print("*     1. Play Game     *")
print("*       2. Exit        *")
print("* * * * * * * * * * * * ")

userInput = input("Make your choice: ")
print("\n")

match userInput:
    case "1":
        playGame()
    case "2":
        print("Thanks for playing!")
    case _:
        print("Invalid entry")
