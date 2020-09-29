# Project Y


# Generate 100 random numbers
# 1. Filter out the fibonacci numbers
# 2. Filter out those numbers which are divisible by any of the last 7 of the
#    first 12 fibonacci numbers


import random
from fibo import checkfibo, genfibo

# input

R = []
for i in range(100):
    R.append(random.randint(1, 100))

# Process

L1 = []
for n in R:
    if(checkfibo(n) == (0, 0)):
        L1.append(n)



L2 = []
F = genfibo(12)
for n in R:
    for fn in F[-7:]:
        if(n % fn == 0):
            L2.append(n)
            break

# output

print('Objective 1: ', L1)
print('Objective 2: ', L2)
