#  File: EasterSunday.py
#  Description: Program takes in year input to output month and day of Easter Sunday that year.
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created:09/06/18
#  Date Last Modified:09/07/18

###main function computes date of Easter Sunday for a specified year###
def main():
    #input desired year, y
	y = int(input("Enter Year: "))
	a = y%19
	b = y//100
	c = y%100
	d = b//4
	e = b%4
	g = (8*b+13)//25
	h = (19*a+b-d-g+15)%30
	j = c//4
	k = c%4
	m = (a+11*h)//319
	r = (2*e+2*j-k-h+m+32)%7
	#calculates Easter Sunday Month
	n = (h-m+r+90)//25
    #calculates Easter Sunday Day
	p = (h-m+r+n+19)%32
	print ("In %s Easter Sunday is on month %s and day %s" %(y,n,p))

main()
