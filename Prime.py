def isPrime(n):

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

#prints first 50 prime numbers
def main():

    i = 2
    numPrimes = 0
    while numPrimes <= 50:
        if isPrime(i):
            numPrimes += 1
            print(str(numPrimes)+".",i,"is prime")

        i += 1

main()
