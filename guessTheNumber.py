import random
userGuess = int(input("WELCOME TO THE GUESSING NUMBER GAME. GUESS ANY NUMBER BETWEEN 0-100 - "))
num = random.randrange(0,100)
noOfGuesses = 10
while noOfGuesses >= 1:
    if userGuess > num:
        print("High")
        userGuess = int(input("Guess again - "))
    elif userGuess < num:
        print("Low")
        userGuess = int(input("Guess again - "))
    else:
        print("Correct!")
        break
    if noOfGuesses == 1:
        print("The correct answer is " , num)
    noOfGuesses -= 1
    print("No. of guess remaining: " , noOfGuesses)
    
        