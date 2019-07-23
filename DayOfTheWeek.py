#  File: DayOfTheWeek.py
#  Description: Outputs day of the week given a year, month, and day.
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 9/26/18
#  Date Last Modified: 9/26/18

def main():
    #asks operator for year, month, and day input
    year = int(input("Please enter the year (an integer): "))
    month = str(input("Please enter the month (a string): "))
    day = int(input("Please enter the day (an integer): "))

    #sets variable a depending on month of the year
    if month == "Janurary":
        a = 11
    elif month == "February":
        a = 12
    elif month == "March":
        a = 1
    elif month == "April":
        a = 2
    elif month == "May":
        a = 3
    elif month == "June":
        a = 4
    elif month == "July":
        a = 5
    elif month == "August":
        a = 6
    elif month == "September":
        a = 7
    elif month == "October":
        a = 8
    elif month == "November":
        a = 9
    else:
        a = 10

    #sets variable b as the day of the month exactly
    b = day

    #sets variable c as last two digits of year
    if month == "Janurary" or month == "February":
        year -= 1 #subtracts 1 from year if month is Jan or Feb to account for leap years
        c = year%100
    else:
        c = year%100

    #sets variable d as first two digits of year
    d = year//100

    #solves for r, used to give the day of the week
    w = (13*a-1)//5
    x = c//4
    y = d//4
    z = w+x+y+b+c-2*d
    r = z%7
    r = (r+7)%7

    #assign r to a day of the week
    if r == 0:
        dayofweek = "Sunday"
    elif r == 1:
        dayofweek = "Monday"
    elif r == 2:
        dayofweek = "Tuesday"
    elif r == 3:
        dayofweek = "Wednesday"
    elif r == 4:
        dayofweek = "Thursday"
    elif r == 5:
        dayofweek = "Friday"
    else:
        dayofweek = "Saturday"

    print ("The day of the week is " + dayofweek + ".")

main()

    
    
                
