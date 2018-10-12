import random

def playAgain(Status):
    victoryStatus = "Status"
    again = input("YOU "+ Status +". PRESS Y TO PLAY AGAIN")
    if again == "y":
        runGame()
    else:
        print("GOODBYE")

def runGame():
    count = 5
    guessableValue = random.randint(1, 10)
    while count != 0:
        guess = input("GIVE ME A NUMBER")
        if guess == "DEBUG":
            print("Debug mode enabled: Target number is: " + str(guessableValue))
            guess = input("GIVE ME A NUMBER")
        guessInt = int(guess)
        if guessInt == guessableValue:
            playAgain("WIN")
        else:
            print("INCORRECT")
            count = count -1
    playAgain("LOSE")

runGame()