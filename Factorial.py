def main():

    number = int(input("Enter a number: "))
    #sentinel value will be -1
    while number != -1:

        fact = 1
    
        for i in range(1,number+1):
            fact *= i
        
        print ("The factorial of",number,"is",fact)
        #User Confirmation to keep code running if desired
        number = int(input("Enter a number: "))

main()
                 
