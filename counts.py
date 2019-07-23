def main():

    numbers = 101* [0]

    value = input("Enter a number: ")
    while value != "":
        numbers = [int(value)] + 1
        value = input("Enter the next number: ")

    for i in range(1,101):
        if number[i] != 0:
            print("The number of",str(i)+"'s is", numbers)
    


main()
