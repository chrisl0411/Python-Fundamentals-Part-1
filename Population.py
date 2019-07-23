#  File: Population.py
#  Description: HW15: Population
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: grizzlee19
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 12/3/18
#  Date Last Modified: 12/5/18

def main():

    #reads text file and initialize dictionary counter
    censusData = open("2009CensusData.txt","r")
    char = censusData.readline()
    firstDigitCount = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

    #iterates through each line and stops at the first digit found
    while char != "":
        if char.isdigit():
            firstDigit = char
            for key in firstDigitCount:
                if key == firstDigit:
                    firstDigitCount[key] += 1
            char = censusData.readline()
            char = censusData.read(1)
        elif char == "\n":
            char = censusData.read(1)
        else:
            char = censusData.read(1)
    
    #header
    print(format("Digit","5s")+format("Count",">8s")+format("%",">6s"))
    print("-"*21)

    #extracts total population, digit, count, and relative frequency
    totalPop = 0
    for value in firstDigitCount.values():
        totalPop += value
    
    for key,value in firstDigitCount.items():
        relFreq = (value/totalPop)*100
        print(format(key,"1s")+format(value,">12d")+format(relFreq,">8.1f"))
    print("")
        
main()
