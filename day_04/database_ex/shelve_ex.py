import shelve

D = { 'name':'Ram', 'age':35, 'country':'Netherlands' }
L = ['red', 'green', 'blue']
L1 = ['Black', 'White', 'Grey']
M = [[1, 2, 4], [1, 3, 5], [6, 7, 8]]

f = shelve.open("mydata")

f['dict'] = D
f['colorlist'] = (L, L1)
f['matrix'] = M

f.sync()
f.close()
