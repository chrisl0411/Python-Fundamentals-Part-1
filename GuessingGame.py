#  File: GuessingGame.py
#  Description: Guessing game that allows player 10 tries to guess the secret number.
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: grizzlee19
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 09/29/18
#  Date Last Modified: 09/29/18

###Loops through ten tries for user to correctly input secret number###
def main():
    #sn is secret number
    sn = 1458
    count = 1
    print("Welcome to the guessing game. You have ten tries to guess my number.")
    n = int(input("Please enter your guess: "))

    #for loop iterating up to 10 times to provide feedback based on guesses
    while count < 11:   
        #checks if number is negative or greater than 10000
        if n < 1 or n > 10000:
            print ("Your guess must be between 0001 and 9999.")
            n = int(input("Please enter a valid guess: "))
        #proceeds with number check indicating as correct, too low or too high
        else:
            if count == 1 and n == sn:
                print ("That's correct! \nCongratulations! You guessed it on the first try!")
                break
            elif n == sn:
                print ("That's correct! \nCongratulations! You guessed it in",count,"guesses.")
                break
            elif n < sn:
                print ("Your guess is too low. \nGuesses so far:",count)
                if count == 10:
                    print ("Game over: you ran out of guesses.")
                    break
                else:
                    n = int(input("Please enter your guess: "))
                    count += 1
            else:
                print("Your guess is too high. \nGuesses so far:",count)
                if count == 10:
                    print ("Game over: you ran out of guesses.")
                    break
                else:
                    n = int(input("Please enter your guess: "))
                    count += 1
                                                        
main()
