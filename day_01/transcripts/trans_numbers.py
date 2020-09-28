Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello Oracle!')
Hello Oracle!
>>> for c in 'Oracle':
	print(c)

	
O
r
a
c
l
e
>>> # NUMBERS
>>> 
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 'python'
>>> type(a)
<class 'str'>
>>> 
>>> a = 1.5
>>> type(a)
<class 'float'>
>>> 
>>> 
>>> # -------------------------------- Treatment of numbers
>>> 
>>> # ----------------- Operators
>>> 
>>> # Arithmetic operator
>>> 
>>> a = 10
>>> b = 2
>>> c = a + b
>>> print(c)
12
>>> c
12
>>> a + b
12
>>> a - b
8
>>> a * b
20
>>> a / b
5.0
>>> a %
SyntaxError: invalid syntax
>>> a % 3
1
>>> a // 4
2
>>> a ** b
100
>>> 
>>> 
>>> # Relational operators
>>> 
>>> a > b  # Is the value in a greater than the value in b?
True
>>> c = True
>>> type(c)
<class 'bool'>
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a != b
True
>>> a == b**3 + b
True
>>> 
>>> 
>>> # Logical
>>> 
>>> a < b and a > 5
False
>>> a
10
>>> b
2
>>> a < b or a > 5
True
>>> not(a < b or a > 5)
False
>>> 
>>> 
>>> # Chaining of operators
>>> 
>>> a
10
>>> b
2
>>> a > 5 and a < 10
False
>>> 5 < a < 10
False
>>> 
>>> 
>>> # Caution!!
>>> 
>>> a = 10
>>> b = a ** 0.5
>>> b
3.1622776601683795
>>> a == (b * b)
False
>>> a
10
>>> b * b
10.000000000000002
>>> 
>>> # ------------------------------------ in-built functions
>>> 
>>> a = 100
>>> type(a)
<class 'int'>
>>> float(a)
100.0
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> 
>>> 
>>> b = '0b1100100'
>>> o = '0o144'
>>> h = '0x64'
>>> 
>>> int(b)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '0b1100100'
>>> type(b)
<class 'str'>
>>> int(b, 2)
100
>>> int(o, 8)
100
>>> int(h, 16)
100
>>> 
>>> int("1234")
1234
>>> int("1234", 8)
668
>>> int("1234", 16)
4660
>>> int("1234", 2)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    int("1234", 2)
ValueError: invalid literal for int() with base 2: '1234'
>>> 
>>> 3-2
1
>>> 2-3
-1
>>> abs(3-2)
1
>>> abs(2-3)
1
>>> # ---------------------------------- inbuilt modules
>>> 
>>> 
>>> ang = 90
>>> sin(ang)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    sin(ang)
NameError: name 'sin' is not defined
>>> import math
>>> math.sin(ang)
0.8939966636005579
>>> math.sin(ang * 3.14/180)
0.9999996829318346
>>> math.sin(ang * 3.14159/180)
0.9999999999991198
>>> math.sin(ang * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> 
>>> 
>>> import random
>>> random.randint(1, 100)
66
>>> random.randint(1, 100)
5
>>> random.randint(1, 100)
60
>>> random.randint(1, 100)
8
>>> random.randint(1, 100)
56
>>> random.randint(1, 100)
24
>>> 
>>> f1 = Fraction(1, 2)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    f1 = Fraction(1, 2)
NameError: name 'Fraction' is not defined
>>> from fractions import Fraction
>>> 
>>> f1 = Fraction(1, 2)
>>> f2 = Fraction(1, 4)
>>> f1 + f2
Fraction(3, 4)
>>> f3 = f1 + f2
>>> type(f3)
<class 'fractions.Fraction'>
>>> Fraction('a', 'b')
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    Fraction('a', 'b')
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\fractions.py", line 174, in __new__
    raise TypeError("both arguments should be "
TypeError: both arguments should be Rational instances
>>> Fraction('1.5')
Fraction(3, 2)
>>> Fraction(1.5)
Fraction(3, 2)
>>> 
