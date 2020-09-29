# -------------------------------------------------
# LAB 1
# -------------------------------------------------

L = ['red', 'red', 'green', 'blue', 'orange']

# Removed one red: ['red', 'green', 'blue', 'orange']
L.remove('red')

# 'golden' was added: ['red', 'green', 'blue', 'orange', 'golden']
L.append('golden')

# ----------------- ['green', 'golden', 'blue', 'orange', 'red']


# reversed every item

'''
temp = []
for item in L:
    temp.append(item[::-1])

L = temp
'''

L = [item[::-1] for item in L]

# reverse sorted

L.sort(reverse=True)


print(L)



# OUTPUT > ['neerg', 'nedlog', 'eulb', 'egnaro', 'der']

