Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Inputs
>>> 
>>> input()
435
'435'
>>> a = input()
345
>>> print(a)
345
>>> a
'345'
>>> a + 10
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a + 10
TypeError: can only concatenate str (not "int") to str
>>> int(a) + 10
355
>>> float(a) + 10
355.0
>>> a + str(10)
'34510'
>>> 
>>> 
>>> a = int(input())
345
>>> a + 10
355
>>> a = int(input())
dfg
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'dfg'
>>> 
>>> 
>>> a = int(input('Enter a number: '))
Enter a number: 435
>>> a + 10
445
>>> 
>>> 
>>> # Output
>>> 
>>> print('Hello')
Hello
>>> print(a)
435
>>> print('The final value is : ', a + 10)
The final value is :  445
>>> print('The input value is %d the coeff is %d the final value is %d' % (a, 10, a+10))
The input value is 435 the coeff is 10 the final value is 445
>>> 
