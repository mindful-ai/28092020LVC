# project x
# Objective: Collect some numbers from the user
# Separate the primes, evens and odd numbers

from myprime import checkprime
print('projectx.py __name__ = ', __name__)

# user defined function

def getfloat(s):
    L = s.split('.')
    if(len(L) == 2):
        if(L[0].isdigit() and L[1].isdigit()):
            return True
    else:
        return False

# input

print('Enter your data:')
L = []
while True:
    n = input('# q to quit')
    if(n.lower() == 'q'):
        break
    else:
        if(n.isdigit()):
            L.append(int(n))
        '''
        elif(getfloat(n)):
            L.append(float(n))
        '''

print('-' * 50)
print('VALID DATA ENTERED: \n', L)
    

# process
primes = []
odds = []
evens = []
for n in L:
    if(checkprime(n)):
        primes.append(n)
        
    if(n % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)

# output

print('-' * 50)
print('PRIMES: ', primes)
print('ODDS  : ', odds)
print('EVENS : ', evens)
