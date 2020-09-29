Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------------------ Special functions
>>> # map(), filter() and zip()
>>> 
>>> T = [100, 35, 67, 99, 120]
>>> F = []
>>> for t in T:
	temp = t * 1.8 + 32
	F.append(temp)

	
>>> F
[212.0, 95.0, 152.60000000000002, 210.20000000000002, 248.0]
>>> 
>>> def c2f(t):
	return t * 1.8 + 32

>>> c2f(100)
212.0
>>> F1 = map(c2f, T)
>>> F1
<map object at 0x000002ACBDAB0240>
>>> list(F1)
[212.0, 95.0, 152.60000000000002, 210.20000000000002, 248.0]
>>> 
>>> func = lambda t : t * 1.8 + 32
>>> type(func)
<class 'function'>
>>> 
>>> 
>>> T
[100, 35, 67, 99, 120]
>>> F = map(lambda t : t * 1.8 + 32, T)
>>> F
<map object at 0x000002ACBDAC9C50>
>>> list(F)
[212.0, 95.0, 152.60000000000002, 210.20000000000002, 248.0]
>>> 
>>> 
>>> func(100)
212.0
>>> 
>>> # -------------------------
>>> 
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> L11 = filter(lambda x : (x % 11 == 0), L)
>>> L11
<filter object at 0x000002ACBDAC9C88>
>>> list(L11)
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> 0, 11, 22, 33, 44, 55, 66, 77, 88, 99
(0, 11, 22, 33, 44, 55, 66, 77, 88, 99)
>>> 
>>> # -----------------------------
>>> 
>>> T1 = ('Anil', 'Sunil', 'Raj')
>>> T2 = ('Bangalore', 'Mysore', 'Coorg')
>>> list(zip(T1, T2))
[('Anil', 'Bangalore'), ('Sunil', 'Mysore'), ('Raj', 'Coorg')]
>>> dict(zip(T1, T2))
{'Anil': 'Bangalore', 'Sunil': 'Mysore', 'Raj': 'Coorg'}
>>> dict(zip(T2, T1))
{'Bangalore': 'Anil', 'Mysore': 'Sunil', 'Coorg': 'Raj'}
>>> 
>>> 
>>> D = {'name':'Anil', 'age':35, 'company':'Oracle' }
>>> D.keys()
dict_keys(['name', 'age', 'company'])
>>> D.values()
dict_values(['Anil', 35, 'Oracle'])
>>> 
>>> 
>>> list(zip(*D.items()))
[('name', 'age', 'company'), ('Anil', 35, 'Oracle')]
>>> T = [('Anil', 'Bangalore'), ('Sunil', 'Mysore'), ('Raj', 'Coorg')]
>>> list(zip(*T))
[('Anil', 'Sunil', 'Raj'), ('Bangalore', 'Mysore', 'Coorg')]
>>> 
>>> 
>>> # -----------------------------------------
>>> 
>>> T1
('Anil', 'Sunil', 'Raj')
>>> enumerate(T1)
<enumerate object at 0x000002ACBDACBBD0>
>>> list(enumerate(T1))
[(0, 'Anil'), (1, 'Sunil'), (2, 'Raj')]
>>> list(enumerate(T1, start=5))
[(5, 'Anil'), (6, 'Sunil'), (7, 'Raj')]
>>> 
>>> # -----------------------------------------
>>> 
>>> x = 45
>>> eval('x * 1.8 + 32')
113.0
>>> 
>>> 
>>> # -----------------------------------------
>>> 
>>> pycode = '''
x = 45
y = 35
z = x + y ** 2
'''
>>> exec(pycode)
>>> pycode = '''
x = 45
y = 35
z = x + y ** 2
print(x, y, z)
'''
>>> exec(pycode)
45 35 1270
>>> 
>>> 
>>> # -----------------------------------------
>>> 
>>> pycode
'\nx = 45\ny = 35\nz = x + y ** 2\nprint(x, y, z)\n'
>>> compile(pycode, '', 'exec')
<code object <module> at 0x000002ACBDA968A0, file "", line 2>
>>> c = compile(pycode, '', 'exec')
>>> c
<code object <module> at 0x000002ACBDA969C0, file "", line 2>
>>> exec(c)
45 35 1270
>>> 
