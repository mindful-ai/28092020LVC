# Input some text from the user
# Print the number of every vowel present in the text

# input

text = input('Enter some text: ')

# process

a = 0
e = 0
i = 0
o = 0
u = 0

for c in text:
    if(c.lower() == 'a'):
        a += 1
    elif(c.lower() == 'e'):
        e += 1
    elif(c.lower() == 'i'):
        i += 1
    elif(c.lower() == 'o'):
        o += 1
    elif(c.lower() == 'u'):
        u += 1


# output

print('-'*40)

print('A -----> ', a)
print('E -----> ', e)
print('I -----> ', i)
print('O -----> ', o)
print('U -----> ', u)

