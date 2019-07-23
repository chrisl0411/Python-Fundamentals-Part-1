def justSum(num1,num2):

    total = 0
    for i in range(num1,num2+1):
        total += i

    return total
        

def main():
    
    first = int(input("Enter the first number:"))
    second = int(input("Enter the second number:"))

    total = justSum(first,second)
    print("The total is:",total)

main()
