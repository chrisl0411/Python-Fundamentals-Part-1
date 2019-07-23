def main():

    numbers = []
    value= input("Enter a number: ")

    while value != "":
        numbers.append(int(value))
        value = input("Enter another number: ")

    print("The original list of numbers is: ",numbers)

    for i in range(len(numbers)-1,-1,-1):
        print(numbers[i])
    

main()
    
