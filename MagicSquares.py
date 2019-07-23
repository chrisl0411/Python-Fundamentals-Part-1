#  File: MagicSquares.py
#  Description: HW13: Magic Squares
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: XXXXXXXXXX
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 11/11/18
#  Date Last Modified: 11/15/18

#magicSquare function assigns position of number i 
def magicSquare(n,grid):
    rowIndex = 0 #initial row
    colIndex = n//2 #initial column
    grid[rowIndex][colIndex] = 1
    for i in range(2,(n**2)+1):
        if i == (n**2)+1:
            break
        elif i % n == 1:
            if rowIndex == n-1:
                rowIndex = 0
            else:
                rowIndex += 1
        else:
            if rowIndex == 0:
                rowIndex = n-1
                if colIndex == n-1:
                    colIndex = 0
                else:
                    colIndex += 1
            else:
                rowIndex -= 1
                if colIndex == n-1:
                    colIndex = 0
                else:
                    colIndex += 1
        grid[rowIndex][colIndex] = i
    magicSquare = grid
    return magicSquare

#class MagicSquare initially populates square grid of specified size and uses magicSquare function to get Magic Square
class MagicSquare:

    def __init__(self,side):
        self.side = side
        self.grid = []
        for row in range(self.side):
            self.r = []
            for col in range(self.side):
                self.r.append(0)
            self.grid.append(self.r)
        self.magicSquare = magicSquare(self.side,self.grid) 

    def display(self):
        for row in range(self.side):
            for col in range(self.side):
                print(format(self.grid[row][col],"5d"),end = "")
            print("")

def main():

    for side in range(1,14,2):
        mSquare = MagicSquare(side)
        print("Magic Square of size",side)
        print("")
        mSquare.display()
        print("")

main()
