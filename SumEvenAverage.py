def main():

    number = int(input("Enter a positive number: "))
    total = 0
    x = 0
    for i in range(number+1):
        if i % 2 == 0:
            #i is even
            total += i
            x += 1

        else:
            #i is odd
    #average = total/x

    print("The average is",average)


main()
