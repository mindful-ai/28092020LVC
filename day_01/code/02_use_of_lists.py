# Create 100 random numbers
# Extract all the numbers divisible by 7 and 11

import random

# input

L = []
for i in range(500):
    L.append(random.randint(1, 1000))
print(L)

# process

D = []
for n in L:
    if(n % 7 == 0 and n % 6 == 0):
        D.append(n)

# output

print('-'*50)
print('DIV:')
print(D)
