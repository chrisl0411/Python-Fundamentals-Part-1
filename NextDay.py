#  File: NextDay.py
#  Description:
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 9/19/18
#  Date Last Modified:


###main function outputs the next day's month, day, and year###
#y-year, m-month, d- day, ny-newyear, nm-newmonth, nd-newday
def main():
    y = int(input("Please enter the year: "))
    m = str(input("Please enter the month: "))
    d = int(input("Please enter the day: "))
    isleapyear = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    #Conditional statements computing next day's year
    if m == "December" and d == 31:
        ny = y + 1
    else:
        ny = y
    
    #Conditional statements computing next day's month
    if m == "April" or m == "June" or m == "September" or m == "November":
        if d == 30:
            if m == "April":
                nm = "May"
            elif m == "June":
                nm = "July"
            elif m == "September":
                nm = "October"
            else:
                nm = "December"
        else:
            nm = m
    elif m == "Janurary" or m=="March" or m== "May" or m=="July" or m=="August" or m=="October" or m=="December":
        if d == 31:
            if m == "January":
                nm = "February"
            elif m == "March":
                nm = "April"
            elif m == "May":
                nm = "June"
            elif m == "July":
                nm = "August"
            elif m == "August":
                nm = "September"
            elif m == "October":
                nm = "November"
            else:
                nm = "Janurary"
        else:
            nm = m
    else:
        nm = m

    #Conditional statements computing the next day
    if m == "February":
        if isleapyear and d == 28:
            nd = 29
        elif isleapyear and d == 29:
            nd = 1
            nm = "March"
        elif d == 28:
            nd = 1
            nm = "March"
        elif isleapyear == False and d ==29:
            print("Year is not a leap year. This date does not exist.")
        else:
            nd = d + 1

    elif m == "April" or m=="June" or m=="September" or m=="November":
        if d == 30:
            nd = 1
        else:
            nd = d + 1
    else:
        if d == 31:
            nd = 1
        else:
            nd = d + 1

    print ("The next day is %s %s, %s." %(nm,nd,ny))

main()
