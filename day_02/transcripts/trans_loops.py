Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for c in 'python':
	print(c.upper(), end=' ')

	
P Y T H O N 
>>> for item in ['red', 'green', 'blue']:
	print(item[::-1], end=' ')

	
der neerg eulb 
>>> for item in ('red', 'green', 'blue'):
	print(item[::-1], end=' ')

	
der neerg eulb 
>>> for item in {'red', 'green', 'blue'}:
	print(item[::-1], end=' ')

	
der eulb neerg 
>>> 
>>> D = {'name':'Ram', 'age':35, 'company':'oracle' }
>>> for key in D:
	print(key)

	
name
age
company
>>> for key in D.keys():
	print(key)

	
name
age
company
>>> for value in D.values():
	print(value)

	
Ram
35
oracle
>>> for value in D.items():
	print(value)

	
('name', 'Ram')
('age', 35)
('company', 'oracle')
>>> for key, value in D.items():
	print(str(key).ljust(10) + ' | ' + str(value).ljust(20))

	
name       | Ram                 
age        | 35                  
company    | oracle              
>>> 
>>> 
>>> # ------------------------------ Loop control statements
>>> 
>>> for c in 'python':
	print(c, end=' ')

	
p y t h o n 
>>> for c in 'python':
	if( c == 't' ):
		break
	print(c, end=' ')

	
p y 
>>> for c in 'python':
	if( c == 't' ):
		continue
	print(c, end=' ')

	
p y h o n 
>>> 
>>> 
>>> # --------------------------- Loop else block
>>> 
>>> for c in 'python':
	if( c == 't'):
		break
	print(c, end=' ')
else:
	print('Completed')

	
p y 
>>> for c in 'python':
	if( c == 'z'):
		break
	print(c, end=' ')
else:
	print('Completed')

	
p y t h o n Completed
>>> 
>>> 
>>> # ------------------------------ consecutive numbers
>>> 
>>> 
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 30, 2))
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> list(range(30, 10, -1))
[30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> 
>>> for i in range(1, 11):
	print('5 X ' + str(i) + ' = ' + str(5 * i))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
>>> # ------------------------------------------ while
>>> 
>>> i = 1
>>> while i <= 10:
	print('5 X ' + str(i) + ' = ' + str(5 * i))
	i += 1

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
