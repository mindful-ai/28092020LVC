C:\Users\Purushotham\Desktop\oracle\day_04\labs>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess
>>> c = subprocess.call('dir', shell=True)
 Volume in drive C is Windows
 Volume Serial Number is 68CD-4284

 Directory of C:\Users\Purushotham\Desktop\oracle\day_04\labs

01-10-2020  13:44    <DIR>          .
01-10-2020  13:44    <DIR>          ..
01-10-2020  15:03               895 chat_client.py
01-10-2020  15:03             1,317 chat_server.py
01-10-2020  10:53               746 extract_details.py
01-10-2020  10:27               991 resume.txt
               4 File(s)          3,949 bytes
               2 Dir(s)  184,519,258,112 bytes free
>>> c
0
>>> c = subprocess.call('ddd', shell=True)
'ddd' is not recognized as an internal or external command,
operable program or batch file.
>>> c
1
>>> # ---------------------------------
...
>>> c = subprocess.check_output("dir", shell=True)
>>> c
b' Volume in drive C is Windows\r\n Volume Serial Number is 68CD-4284\r\n\r\n Directory of C:\\Users\\Purushotham\\Desktop\\oracle\\day_04\\labs\r\n\r\n01-10-2020  13:44    <DIR>          .\r\n01-10-2020  13:44    <DIR>          ..\r\n01-10-2020  15:03               895 chat_client.py\r\n01-10-2020  15:03             1,317 chat_server.py\r\n01-10-2020  10:53               746 extract_details.py\r\n01-10-2020  10:27               991 resume.txt\r\n               4 File(s)          3,949 bytes\r\n               2 Dir(s)  184,518,844,416 bytes free\r\n'
>>> print(c)
b' Volume in drive C is Windows\r\n Volume Serial Number is 68CD-4284\r\n\r\n Directory of C:\\Users\\Purushotham\\Desktop\\oracle\\day_04\\labs\r\n\r\n01-10-2020  13:44    <DIR>          .\r\n01-10-2020  13:44    <DIR>          ..\r\n01-10-2020  15:03               895 chat_client.py\r\n01-10-2020  15:03             1,317 chat_server.py\r\n01-10-2020  10:53               746 extract_details.py\r\n01-10-2020  10:27               991 resume.txt\r\n               4 File(s)          3,949 bytes\r\n               2 Dir(s)  184,518,844,416 bytes free\r\n'
>>> c = c.decode()
>>> print(c)
 Volume in drive C is Windows
 Volume Serial Number is 68CD-4284

 Directory of C:\Users\Purushotham\Desktop\oracle\day_04\labs

01-10-2020  13:44    <DIR>          .
01-10-2020  13:44    <DIR>          ..
01-10-2020  15:03               895 chat_client.py
01-10-2020  15:03             1,317 chat_server.py
01-10-2020  10:53               746 extract_details.py
01-10-2020  10:27               991 resume.txt
               4 File(s)          3,949 bytes
               2 Dir(s)  184,518,844,416 bytes free

>>> type(c)
<class 'str'>
>>> import re
>>> pattern = r"\d\d:\d\d"
>>> re.findall(pattern, c)
['13:44', '13:44', '15:03', '15:03', '10:53', '10:27']
>>>


