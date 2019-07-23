def main():

    numberString = input("Enter 5 numbers separated by spaces: ")
    numberList = numberString.split()

    total = 0
    for num in numberList:
        total += int(num)
    average = total/5
    
    print(numberString)
    print(numberList)
    print("The average is: ",average)


main()
