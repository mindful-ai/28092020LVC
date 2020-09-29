# -------------------------------------------------
# LAB 3 - Word Jumble Game
# -------------------------------------------------

import random

def jumble(s):
    temp = list(s)
    random.shuffle(temp)
    return ''.join(temp)

print('----------------------------------------------')
print('               WORD JUMBLE GAME               ')
print('----------------------------------------------')

# Create a word list
words = ['laptop', 'clock', 'books', 'paper', 'pencil']

score = 0

# Loop
for word in words:
    
    # Pick a word
    # Jumble the word
    jword = jumble(word)
    
    # Present it to the user
    print('Can you guess this? ', jword)
    
    # Ask for the user's guess
    uword = input('? ')
    
    # Compare and give result
    if(uword == word):
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    print('_'*30)

# Give the final score

print('\n\n----------------------------------------------')
print('SCORE: ', score)
if( score > 3 ):
    print('Excellent')
else:
    print('Improvement needed')

print('----------------------------------------------')
