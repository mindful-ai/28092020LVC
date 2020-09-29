Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'m', 'p', 's', 'i'}
>>> 
>>> 
>>> # ==================
>>> 
>>> s1 = set('abcdefg')
>>> s1
{'a', 'b', 'd', 'f', 'e', 'c', 'g'}
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}
>>> s2
{'d', 'i', 'f', 'h', 'e', 'j', 'g'}
>>> 
>>> 
>>> s1 | s2
{'a', 'b', 'd', 'i', 'f', 'h', 'e', 'c', 'j', 'g'}
>>> s1 & s2
{'e', 'd', 'g', 'f'}
>>> s1 ^ s2
{'i', 'c', 'a', 'b', 'h', 'j'}
>>> 
>>> 
>>> s1.add('x')
>>> s1
{'a', 'b', 'd', 'f', 'e', 'c', 'x', 'g'}
>>> s1.update({'y', 'z'})
>>> s1
{'a', 'b', 'd', 'f', 'e', 'c', 'x', 'y', 'z', 'g'}
>>> s1.remove('g')
>>> s1
{'a', 'b', 'd', 'f', 'e', 'c', 'x', 'y', 'z'}
>>> len(s1)
9
>>> 'a' in s1
True
>>> 
>>> for item in s1:
	print(item)

	
a
b
d
f
e
c
x
y
z
>>> s3 = { 'a', 'b', 'red', 1.4, [1, 2, ,3] }
SyntaxError: invalid syntax
>>> s3 = { 'a', 'b', 'red', 1.4, [1, 2, 3] }
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s3 = { 'a', 'b', 'red', 1.4, [1, 2, 3] }
TypeError: unhashable type: 'list'
>>> s3 = { 'a', 'b', 'red', 1.4 }
>>> S3
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    S3
NameError: name 'S3' is not defined
>>> s3
{'a', 'b', 1.4, 'red'}
>>> s3.add([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s3.add([1, 2, 3])
TypeError: unhashable type: 'list'
>>> s3.add(True)
>>> s3
{'a', 'b', 1.4, True, 'red'}
>>> 
>>> 
>>> 
>>> # -----------------------------------
>>> 
>>> L = [ 'red', 'green', [ 'skyblue', 'cerulean', 'deepblue' ], [ ['yellow', 'golden'], ['orange', 'brown']]]
>>> L
['red', 'green', ['skyblue', 'cerulean', 'deepblue'], [['yellow', 'golden'], ['orange', 'brown']]]
>>> L.append(set('red'))
>>> L
['red', 'green', ['skyblue', 'cerulean', 'deepblue'], [['yellow', 'golden'], ['orange', 'brown']], {'d', 'r', 'e'}]
>>> L.append(tuple('orange'))
>>> L
['red', 'green', ['skyblue', 'cerulean', 'deepblue'], [['yellow', 'golden'], ['orange', 'brown']], {'d', 'r', 'e'}, ('o', 'r', 'a', 'n', 'g', 'e')]
>>> L[-1]
('o', 'r', 'a', 'n', 'g', 'e')
>>> L[-2]
{'d', 'r', 'e'}
>>> tuple(L)
('red', 'green', ['skyblue', 'cerulean', 'deepblue'], [['yellow', 'golden'], ['orange', 'brown']], {'d', 'r', 'e'}, ('o', 'r', 'a', 'n', 'g', 'e'))
>>> T = tuple(L)
>>> type(T)
<class 'tuple'>
>>> type(L)
<class 'list'>
>>> type(s1)
<class 'set'>
>>> # ------------------------------------- Hrushikesh
