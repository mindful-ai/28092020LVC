Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ("red", "green", "blue")
>>> type(T)
<class 'tuple'>
>>> 
>>> 
>>> T[0]
'red'
>>> T[1:2]
('green',)
>>> T[::-1]
('blue', 'green', 'red')
>>> 
>>> # ------------------------------
>>> 
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> sorted(T)
['blue', 'green', 'red']
>>> 
>>> 
>>> # ------------------------------
>>> 
>>> T
('red', 'green', 'blue')
>>> L = list(T)
>>> L
['red', 'green', 'blue']
>>> L.append('yellow')
>>> L
['red', 'green', 'blue', 'yellow']
>>> T = tuple(L)
>>> T
('red', 'green', 'blue', 'yellow')
>>> 
>>> # --------------------------------- unpacking
>>> 
>>> T
('red', 'green', 'blue', 'yellow')
>>> r, g, b, y = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> y
'yellow'
>>> r, g = T
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    r, g = T
ValueError: too many values to unpack (expected 2)
>>> r, g, *x = T
>>> r
'red'
>>> g
'green'
>>> x
['blue', 'yellow']
>>> 
