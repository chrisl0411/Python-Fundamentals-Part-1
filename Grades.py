#  File: Grades.py
#  Description: HW14: Grade Book
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: grizzlee19
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 11/25/18
#  Date Last Modified: 11/26/18

def main():
    gradesIn = open("gradeInput.txt","r")
    gradesOut = open("gradeOutput.txt","w")
    gradesOut.write(format("Hw",">32s")+format("Exam",">9s")+format("Final",">8s")+"\n")
    gradesOut.write(format("Last Name","<15s")+format("First Name","<15s")+format("Avg","<7s")+format("Avg","<7s")+format("Grade","<7s")+"\n")
    gradesOut.write("-"*51+"\n")    
    char = gradesIn.read(1)

    #extracts and assigns information from file
    while char != "":
        #reads and assigns last name
        lastName = ""
        while char != ",":
            lastName += char
            char = gradesIn.read(1)
        #reads and assigns first name
        char = gradesIn.read(1)
        firstName = ""
        while char != " ":
            firstName += char
            char = gradesIn.read(1)
        char = gradesIn.read(1)
        #reads and assigns all grades
        allGrades = ""
        while char != "\n":
            allGrades += char
            char = gradesIn.read(1)
            
        #splits all grades into a list and converts strings to integers
        allGrades = allGrades.split()
        for i in range(len(allGrades)):
            allGrades[i] = int(allGrades[i])
        #assigns first 15 grades as hw scores and last 3 grades as test scores
        hwGrades = allGrades[0:15]
        testGrades = allGrades[15:]

        #calculates hw average and test averages
        hwSum = 0
        for i in range(len(hwGrades)):
            hwSum += hwGrades[i]
            hwAverage = hwSum/len(hwGrades)
            
        testSum = 0
        for j in range(len(testGrades)):
            testSum += testGrades[j]
            testAverage = testSum/len(testGrades)

        #calculates final grade
        finalGrade = (hwAverage*0.55)+(testAverage*0.45)

        #write out information to gradeOutput.txt file
        gradesOut.write(format(lastName,"<15s")+format(firstName,"<15s")+format(hwAverage,"<7.1f")+format(testAverage,"<7.1f")+format(finalGrade,"<7.1f")+"\n")
    
        char = gradesIn.read(1)

    gradesIn.close()
    gradesOut.close()
        
main()
