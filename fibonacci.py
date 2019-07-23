def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fn1 = fibonacci(n-1)
        fn2 = fibonacci(n-2)
        print("fibonacci("+str(n)+") =",str(fn1)+" + "+str(fn2))
        return fn1 + fn2

def main():
    
    print(fibonacci(7))

main()
