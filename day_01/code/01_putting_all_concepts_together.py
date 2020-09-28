# Objective: input two numbers from the user
# Determine is the difference of number is positive, negative or zero

# Input

a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))

# Process

res = a - b

# Output

print('------------------------------')
print('DIFFERENCE: ', abs(a / b))
if(res > 0):
    print('The result is positive')  
elif(res < 0):
    print('The result is negative')
else:
    print('The result is zero')
