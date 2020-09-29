Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = list(range(10, 100))
>>> L
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> L10 = []
>>> for n in L:
	if(int(str(n)[1]) + int(str(n)[0]) == 10):
		L10.append(n)

		
>>> L10
[19, 28, 37, 46, 55, 64, 73, 82, 91]
>>> 
>>> LC10 = [x for x in L if (int(str(n)[1]) + int(str(n)[0]) == 10)]
>>> LC10
[]
>>> LC10 = [x for x in L if (int(str(x)[1]) + int(str(x)[0]) == 10)]
>>> LC10
[19, 28, 37, 46, 55, 64, 73, 82, 91]
>>> TC10 = (x for x in L if (int(str(x)[1]) + int(str(x)[0]) == 10))
>>> TC10
<generator object <genexpr> at 0x0000014F5669B930>
>>> tuple(TC10)
(19, 28, 37, 46, 55, 64, 73, 82, 91)
>>> SC10 = {x for x in L if (int(str(x)[1]) + int(str(x)[0]) == 10)}
>>> SC10
{64, 37, 73, 46, 82, 19, 55, 91, 28}
>>> 
>>> 
>>> # ------------------------------------------------------
>>> 
>>> # [<expr> <loop> <condition>]
>>> 
>>> 
>>> E = [p for p in range(101) if (p % 2 == 0)]
>>> E
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> 
>>> LT = [ (n, n**2, n**3) for n in range(1, 11) ]
>>> LT
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729), (10, 100, 1000)]
>>> 
>>> 
>>> L = ['red', 'green', 'blue', 'yellow']
>>> D = { s:len(s) for s in L }
>>> D
{'red': 3, 'green': 5, 'blue': 4, 'yellow': 6}
>>> 
>>> 
>>> N = [1, 2, 3, 4, 5]
>>> LC = [x for x in N if(x % 3 == 0)]
>>> LC
[3]
>>> LC = [x**2 for x in N if(x % 3 == 0)]
>>> LC
[9]
>>> LC = [x**2 if x == 3 else x for x in N]
>>> LC
[1, 2, 9, 4, 5]
>>> type(N)
<class 'list'>
>>> type(LC)
<class 'list'>
>>> LC = (x**2 if x == 3 else x for x in N)
>>> type(LC)
<class 'generator'>
>>> import math
>>> LC = (math.pow(x, 2) if x == 3 else x for x in N)
>>> LC
<generator object <genexpr> at 0x0000014F5669B9A8>
>>> tuple(LC)
(1, 2, 9.0, 4, 5)
>>> 
