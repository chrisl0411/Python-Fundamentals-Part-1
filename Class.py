def squirt(value):
    squirtValue = value ** 0.5
    return squirtValue
    

def main():
    myNumber = int(input("Enter a value: "))
    mySqrt = squirt(myNumber)
    print("The square root is:",mySqrt)
    
main()
