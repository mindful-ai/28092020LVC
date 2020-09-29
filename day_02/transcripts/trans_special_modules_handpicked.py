Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2020, 9, 29, 15, 18, 2, 934221)
>>> datetime.datetime(2020, 9, 29, 15, 18, 2, 934221)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    datetime.datetime(2020, 9, 29, 15, 18, 2, 934221)
AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
>>> t.year
2020
>>> t.month
9
>>> t.day
29
>>> t.hour
15
>>> t.minute
18
>>> t.second
2
>>> # --------------------------
>>> 
>>> # Tuesday, 29 September, 2020 Time -> 3:20 PM
>>> 
>>> f = "%A, %d %B, %Y Time -> %I:%M %p"
>>> t.strftime(f)
'Tuesday, 29 September, 2020 Time -> 03:18 PM'
>>> 
>>> 
>>> # --------------------------
>>> 
>>> datetime.now().strftime(f)
'Tuesday, 29 September, 2020 Time -> 03:26 PM'
>>> 
>>> 
>>> # ----------------------------
>>> t
datetime.datetime(2020, 9, 29, 15, 18, 2, 934221)
>>> t1 = datetime.now()
>>> 
>>> t1 - t
datetime.timedelta(seconds=522, microseconds=544406)
>>> 
>>> 
>>> # ------------------------------------------------- itertools
>>> 
>>> from itertools import permutations, combinations
>>> 
>>> s = 'ABCD'
>>> list(permutations(s))
[('A', 'B', 'C', 'D'), ('A', 'B', 'D', 'C'), ('A', 'C', 'B', 'D'), ('A', 'C', 'D', 'B'), ('A', 'D', 'B', 'C'), ('A', 'D', 'C', 'B'), ('B', 'A', 'C', 'D'), ('B', 'A', 'D', 'C'), ('B', 'C', 'A', 'D'), ('B', 'C', 'D', 'A'), ('B', 'D', 'A', 'C'), ('B', 'D', 'C', 'A'), ('C', 'A', 'B', 'D'), ('C', 'A', 'D', 'B'), ('C', 'B', 'A', 'D'), ('C', 'B', 'D', 'A'), ('C', 'D', 'A', 'B'), ('C', 'D', 'B', 'A'), ('D', 'A', 'B', 'C'), ('D', 'A', 'C', 'B'), ('D', 'B', 'A', 'C'), ('D', 'B', 'C', 'A'), ('D', 'C', 'A', 'B'), ('D', 'C', 'B', 'A')]
>>> L = list(map(lambda t : ''.join(t), permutations(s)))
>>> L
['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']
>>> list(combinations(s))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list(combinations(s))
TypeError: combinations() missing required argument 'r' (pos 2)
>>> list(combinations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
>>> list(permutaions(s, 3))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(permutaions(s, 3))
NameError: name 'permutaions' is not defined
>>> list(permutations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> 
>>> 
>>> # --------------------------------------- functools
>>> 
>>> from functools import reduce
>>> 
>>> L = [1,2,3,4,5]
>>> 
>>> reduce(lambda x,y : x + y, L)
15
>>> 
>>> 
>>> # --------------------------------------
>>> 
>>> 
>>> from statistics import mean, median
>>> 
>>> import random
>>> 
>>> L = [random.randint(1, 100) for i in range(20)]
>>> L.mean()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    L.mean()
AttributeError: 'list' object has no attribute 'mean'
>>> mean(L)
48.9
>>> median(L)
46.5
>>> 
>>> 
>>> # ------------------------------------------
>>> 
>>> from operator import itemgetter
>>> 
>>> itemgetter(1)('apples')
'p'
>>> itemgetter(1)(['apples', 'grapes', 'oranges'])
'grapes'
>>> 
>>> f = itemgetter(1)
>>> f('apples')
'p'
>>> f(['apples', 'grapes', 'oranges'])
'grapes'
>>> 
>>> 
>>> L = ['apples', 'carrot', 'zucchini', 'grapes', 'oranges']
>>> L.sort()
>>> L
['apples', 'carrot', 'grapes', 'oranges', 'zucchini']
>>> 
>>> f = itemgetter(-1)
>>> L.sort(key=f)
>>> L
['zucchini', 'apples', 'grapes', 'oranges', 'carrot']
>>> L.sort(key=itemgetter(1))
>>> L
['carrot', 'apples', 'grapes', 'oranges', 'zucchini']
>>> 
>>> 
