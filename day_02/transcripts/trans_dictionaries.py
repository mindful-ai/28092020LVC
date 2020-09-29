Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = { 'Ram', 35, 'Oracle', 'India' }
>>> s
{'Ram', 'Oracle', 35, 'India'}
>>> D = { 'name':'Ram', 'age':35, 'company':'oracle', 'country': 'India'}
>>> D
{'name': 'Ram', 'age': 35, 'company': 'oracle', 'country': 'India'}
>>> type(D)
<class 'dict'>
>>> 
>>> # -------------------------------------------
>>> 
>>> D['name']
'Ram'
>>> D['age']
35
>>> D['phone']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    D['phone']
KeyError: 'phone'
>>> D['phone'] = '+917645384985'
>>> D
{'name': 'Ram', 'age': 35, 'company': 'oracle', 'country': 'India', 'phone': '+917645384985'}
>>> D.setdefault('addr')
>>> D
{'name': 'Ram', 'age': 35, 'company': 'oracle', 'country': 'India', 'phone': '+917645384985', 'addr': None}
>>> D.setdefault('hobbies',['music', 'cinema'])
['music', 'cinema']
>>> D
{'name': 'Ram', 'age': 35, 'company': 'oracle', 'country': 'India', 'phone': '+917645384985', 'addr': None, 'hobbies': ['music', 'cinema']}
>>> D.setdefault('name')
'Ram'
>>> 
>>> 
>>> D['addr']
>>> D['addr'] = 'Mysore'
>>> D
{'name': 'Ram', 'age': 35, 'company': 'oracle', 'country': 'India', 'phone': '+917645384985', 'addr': 'Mysore', 'hobbies': ['music', 'cinema']}
>>> 
>>> 
>>> D.remove('age')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    D.remove('age')
AttributeError: 'dict' object has no attribute 'remove'
>>> D.pop('age')
35
>>> D
{'name': 'Ram', 'company': 'oracle', 'country': 'India', 'phone': '+917645384985', 'addr': 'Mysore', 'hobbies': ['music', 'cinema']}
>>> 
>>> 
>>> D1 = {'dob':'24-09-1982', 'salary':'1000000 INR'}
>>> D['details'] = D1
>>> D
{'name': 'Ram', 'company': 'oracle', 'country': 'India', 'phone': '+917645384985', 'addr': 'Mysore', 'hobbies': ['music', 'cinema'], 'details': {'dob': '24-09-1982', 'salary': '1000000 INR'}}
>>> D.pop('details')
{'dob': '24-09-1982', 'salary': '1000000 INR'}
>>> D.update(D1)
>>> D
{'name': 'Ram', 'company': 'oracle', 'country': 'India', 'phone': '+917645384985', 'addr': 'Mysore', 'hobbies': ['music', 'cinema'], 'dob': '24-09-1982', 'salary': '1000000 INR'}
>>> 
>>> # ----------------------------------------------------
>>> 
>>> D.keys()
dict_keys(['name', 'company', 'country', 'phone', 'addr', 'hobbies', 'dob', 'salary'])
>>> D.values()
dict_values(['Ram', 'oracle', 'India', '+917645384985', 'Mysore', ['music', 'cinema'], '24-09-1982', '1000000 INR'])
>>> D.items()
dict_items([('name', 'Ram'), ('company', 'oracle'), ('country', 'India'), ('phone', '+917645384985'), ('addr', 'Mysore'), ('hobbies', ['music', 'cinema']), ('dob', '24-09-1982'), ('salary', '1000000 INR')])
>>> 
>>> 
>>> # --------------------------------- iteration
>>> 
>>> for i in D:
	print(i, end=' ')

	
name company country phone addr hobbies dob salary 
>>> for i in D.keys():
	print(i, end=' ')

	
name company country phone addr hobbies dob salary 
>>> for i in D.values():
	print(i, end=' ')

	
Ram oracle India +917645384985 Mysore ['music', 'cinema'] 24-09-1982 1000000 INR 
>>> for i in D.items():
	print(i, end=' ')

	
('name', 'Ram') ('company', 'oracle') ('country', 'India') ('phone', '+917645384985') ('addr', 'Mysore') ('hobbies', ['music', 'cinema']) ('dob', '24-09-1982') ('salary', '1000000 INR') 
>>> 
>>> 
>>> for k, v in D.items():
	print(str(k) + ' ------> ' + str(v))

	
name ------> Ram
company ------> oracle
country ------> India
phone ------> +917645384985
addr ------> Mysore
hobbies ------> ['music', 'cinema']
dob ------> 24-09-1982
salary ------> 1000000 INR
>>> for k, v in D.items():
	print(str(k).ljust(20) + ' | ' + str(v).ljust(20))

	
name                 | Ram                 
company              | oracle              
country              | India               
phone                | +917645384985       
addr                 | Mysore              
hobbies              | ['music', 'cinema'] 
dob                  | 24-09-1982          
salary               | 1000000 INR         
>>> 
>>> 
>>> # -------------------------------- Yeshwanth
>>> 
>>> D
{'name': 'Ram', 'company': 'oracle', 'country': 'India', 'phone': '+917645384985', 'addr': 'Mysore', 'hobbies': ['music', 'cinema'], 'dob': '24-09-1982', 'salary': '1000000 INR'}
>>> D.pop()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    D.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> D.clear()
>>> D
{}
>>> del D
>>> D
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> 
