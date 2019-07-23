#  File: Deal.py
#  Description: Outputs probability of winning the "Lets Make a Deal" game when switching guess. Proves Savant's advice is correct.
#  Student's Name: CHristopher Lee
#  Student's UT EID: cl37976
#  Identifier: grizzlee19
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 10/21/18
#  Date Last Modified: 10/24/18

import random

#function return random number between 1 and n
def roll(n):
    randNumber = random.randint(1,n)
    return randNumber

#function returns result of switching guess and values of prize, guess, view, and new guess
def runOneTrial():
    prize = roll(3)
    guess = roll(3)
    view = prize

    #checks if view is equal to prize and guess, then assigns new value
    if prize == guess:
        while view == prize:
            view = roll(3)
    else:
        while view == prize or view == guess:
            view = roll(3)
        
    #checks if newGuess is equal to view or guess then assigns new value
    newGuess = view
    while newGuess == view or newGuess == guess:
        newGuess = roll(3)

    #assigns "win" or "lose" if new guess is the prize 
    if newGuess == prize:
        result = "win"
    else:
        result = "lose"

    return result, prize, guess, view, newGuess

###main function executes number of trials inputted and calculates probability of winning when switching guess.
def main():
    
    numTrials = int(input("How many trials do you want to run? "))
    print("")
    print(format("Prize","<5s"),format("Guess",">6s"),format("View",">5s"),format("New Guess",">10s"))
    win = 0
    
    for i in range(numTrials):
        result,prize,guess,view,newGuess = runOneTrial()
        print(format(prize,">3d"),format(guess,">6d"),format(view,">6d"),format(newGuess,">8d"))
        if result == "win":
            win += 1

    probSwitch = win/numTrials
    probNotSwitch = 1-probSwitch

    print("Probability of winning if you switch =",format(probSwitch,"3.1f"))
    print("Probability of winning if you do not switch =",format(probNotSwitch,"3.1f"))
    
main()

        
        
