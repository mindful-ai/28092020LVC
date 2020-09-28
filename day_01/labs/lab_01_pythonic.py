# Input some text from the user
# Print the number of every vowel present in the text

# input

text = input('Enter some text: ')

# process
# output

print('-'*50)
for c in 'aeiou':
    print(c.upper() + ' ----------> ' + str(text.count(c)))
    


