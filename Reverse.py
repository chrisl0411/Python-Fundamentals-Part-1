#  File: Reverse.py
#  Description: Reverses 4-digit number's order, using arithmetic operators.
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 09/14/18
#  Date Last Modified: 09/14/18

### Main function takes in 4-digit number input and prints reversed order of digits ###
def main():
    
    #Input 4-digit number
    num = int(input("Enter an integer: "))
    #Extracts individual digits of the 4-digit number
    thousands = num//1000
    ones = num%10
    tens = int((num%100-ones)/10)
    hundreds = int((num%1000-num%100)/100)
    #Prints reversed number
    print("The reversed number is %s%s%s%s." %(ones,tens,hundreds,thousands))
    
main()
    
