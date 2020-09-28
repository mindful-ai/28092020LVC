Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = []
>>> L
[]
>>> type(L)
<class 'list'>
>>> 
>>> L = [1, -2, 4.5, True, 'apples', [1,2,3], len]
>>> 
>>> 
>>> 
>>> # ---------------------------------------------------
>>> 
>>> L = ["red", "green", "blue", "yellow"]
>>> 
>>> # --------------------------- subscripting
>>> 
>>> L[0]
'red'
>>> L[2]
'blue'
>>> L[-1]
'yellow'
>>> L[2:4]
['blue', 'yellow']
>>> L[:2]
['red', 'green']
>>> L[2:]
['blue', 'yellow']
>>> L[:]
['red', 'green', 'blue', 'yellow']
>>> L[::2]
['red', 'blue']
>>> L[::-1]
['yellow', 'blue', 'green', 'red']
>>> 
>>> 
>>> # ------------------------------- mutability
>>> 
>>> L[0]
'red'
>>> L[0] = 'orange'
>>> L
['orange', 'green', 'blue', 'yellow']
>>> 
>>> L[2]
'blue'
>>> L[2][2]
'u'
>>> L[2][2] = 'x'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    L[2][2] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> # List is mutable, but, the elements in the list need not be mutable
>>> 
>>> L = ['red', 'green', ['b', 'l', 'u', 'e']]
>>> L[2][2] = 'x'
>>> L
['red', 'green', ['b', 'l', 'x', 'e']]
>>> 
>>> 
>>> # ----------------------------------- operators
>>> 
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> len(L)
3
>>> L
['red', 'green', ['b', 'l', 'x', 'e']]
>>> 'red' in L
True
>>> del L[0]
>>> L
['green', ['b', 'l', 'x', 'e']]
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> 
>>> # -------------------------------- functions
>>> 
>>> L = ['red', 'green', 'blue']
>>> 
>>> # ---------- adding elements
>>> L
['red', 'green', 'blue']
>>> L.append('yellow')
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append('cyan')
>>> L
['red', 'green', 'blue', 'yellow', 'cyan']
>>> L.insert(1, 'magenta')
>>> L
['red', 'magenta', 'green', 'blue', 'yellow', 'cyan']
>>> L1 = ['purple', 'maroon']
>>> L.extend(L1)
>>> L
['red', 'magenta', 'green', 'blue', 'yellow', 'cyan', 'purple', 'maroon']
>>> 
>>> 
>>> L = ['red', 'green', 'blue']
>>> L[1]
'green'
>>> L[1] = 'yellow'
>>> L
['red', 'yellow', 'blue']
>>> L[1] =  L1
>>> L
['red', ['purple', 'maroon'], 'blue']
>>> 
>>> 
>>> L = ['red', 'green', 'blue']
>>> L[1:2]
['green']
>>> L[1]
'green'
>>> L[1:2] = L1
>>> L
['red', 'purple', 'maroon', 'blue']
>>> 
>>> 
>>> # -------------------------------- removing elelments
>>> 
>>> L
['red', 'purple', 'maroon', 'blue']
>>> L.pop()
'blue'
>>> L
['red', 'purple', 'maroon']
>>> L.pop(1)
'purple'
>>> L
['red', 'maroon']
>>> L = ['red', 'green', 'blue']
>>> L.remove('green')
>>> L
['red', 'blue']
>>> 
>>> 
>>> # --------------------------------- re-oraganizing elements
>>> 
>>> L
['red', 'blue']
>>> L = ['zebra', 'goat', 'fox', 'bear']
>>> 
>>> # ----------------- reverse the list
>>> L[::-1]
['bear', 'fox', 'goat', 'zebra']
>>> reversed(L)
<list_reverseiterator object at 0x000002799E230A58>
>>> list(reversed(L))
['bear', 'fox', 'goat', 'zebra']
>>> 
>>> L
['zebra', 'goat', 'fox', 'bear']
>>> L.reverse()
>>> L
['bear', 'fox', 'goat', 'zebra']
>>> 
>>> # ---------------- sort the list
>>> 
>>> sorted(L)
['bear', 'fox', 'goat', 'zebra']
>>> L
['bear', 'fox', 'goat', 'zebra']
>>> L.add('ant')
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    L.add('ant')
AttributeError: 'list' object has no attribute 'add'
>>> L.append('ant')
>>> L
['bear', 'fox', 'goat', 'zebra', 'ant']
>>> sorted(L)
['ant', 'bear', 'fox', 'goat', 'zebra']
>>> L
['bear', 'fox', 'goat', 'zebra', 'ant']
>>> L.sort()
>>> L
['ant', 'bear', 'fox', 'goat', 'zebra']
>>> L.sort(reverse=True)
>>> L
['zebra', 'goat', 'fox', 'bear', 'ant']
>>> 
>>> 
>>> # ---------------------------- search
>>> 
>>> L
['zebra', 'goat', 'fox', 'bear', 'ant']
>>> 
>>> 'fox' in L
True
>>> L.index('fox')
2
>>> L.index('cat')
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    L.index('cat')
ValueError: 'cat' is not in list
>>> L.count('fox')
1
>>> 
>>> # ------------------------------ numeric lists
>>> 
>>> L = [1, 2, 3, 4, 5]
>>> sum(L)
15
>>> any(L)
True
>>> L = [0, 0, 0, 1, 0]
>>> any(L)
True
>>> all(L)
False
>>> 
>>> 
>>> # -------------------------- iteration
>>> 
>>> for item in L:
	print(item)

	
0
0
0
1
0
>>> L = ['zebra', 'goat', 'fox', 'bear', 'ant']
>>> for item in L:
	print(item.upper(), end=' ')

	
ZEBRA GOAT FOX BEAR ANT 
>>> 
