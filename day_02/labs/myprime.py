def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

# ----------------------------------


print('myprime.py __name__ = ', __name__)

if __name__ == '__main__':

    x = int(input('Enter a number: '))
    if(checkprime(x)):
        print('This number is prime')
    else:
        print('This number is not prime')

        
