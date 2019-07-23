def extremes(num1,num2,num3):
    biggest = max(num1,num2,num3)
    littlest = min(num1,num2,num3)

    return biggest,littlest

def main():

    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    third = int(input("Enter the third number: "))

    #assigns biggest and littlest from extreme function to largest and smallest
    largest,smallest = extremes(first,second,third)

    print("The largest of the numbers is:",largest)
    print("The smallest of the numbers is:",smallest)


main()
