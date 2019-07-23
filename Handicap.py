#  File: Handicap.py
#  Description: Calculates the average and handicap of a bowler's three games.
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 09/10/18
#  Date Last Modified: 09/12/18

### Main function takes in three bowling scores, averages them, and outputs a handicap ###
def main():
    #User inputs three bowling game scores
    a = int(input("Enter Game 1: "))
    b = int(input("Enter Game 2: "))
    c = int(input("Enter Game 3: "))
    #Averages three bowling scores and truncates to lowest integer
    average = (a+b+c)//3
    #Calculates handicap and truncates to lowest integer
    handicap = int((200-average) * 0.80)
    print ("The bowler's average is: ", average)
    print ("The bowler's handicap is: ", handicap)
main()
            
            
            
