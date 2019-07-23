def main():

    numbers = []
    value = input("Enter a number: ")

    while value != "":
        numbers.append(int(value))
        value = input("Enter another number: ")

    print("The list of numbers is: ",numbers)

    average = sum(numbers)/len(numbers)
    print("The average is: "+format(average,"5.2f"))

    biggerNumbers = 0

    for num in numbers:
        if num > average:
            biggerNumbers += 1

    print("The number of values greater than the average is:",biggerNumbers)
    
main()
