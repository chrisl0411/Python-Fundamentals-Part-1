#  File: Combinations.py
#  Description: Program that prints a table listing the number of possible hands of r cards, where r ranges from 0 to 52.
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: grizzlee19
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 10/16/18
#  Date Last Modified: 10/16/18

#calculates the factorial of an input "num"
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i    
    return fact

#calculates the number of combinations possible with n objects taken with r at a time
def combinations(n,r):
    nFact = factorial(n)
    rFact = factorial(r)
    nMinusr = n-r
    nMinusrFact = factorial(nMinusr)

    combo = nFact/(rFact*nMinusrFact)
    return combo

#main function formats output of possible combinations of 52 cards with r number of cards in hand
def main():
    
    print("")
    print(format("Cards","<5s"),format("Combinations",">16s"))
    print("======================")
    n = 52

    for i in range(53):
        combo = combinations(n,i)
        print(format(i,">3d"),format(int(combo),">18d"))
    print("")
    
main()


   
