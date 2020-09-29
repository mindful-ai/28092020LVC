Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILE IO
>>> 
>>> # open(<path>,<mode>) mode -> r, w, a, b
>>> # close()
>>> # read(), readline(), readlines()
>>> # read(), readline(), readlines()
>>> # write(), writelines()
>>> # write(), writelines()
>>> # tell(), seek()
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data.txt")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> path = "c:\text\new\read\t01.txt"
>>> print(path)
c:	ext
ewead	01.txt
>>> path = r"c:\text\new\read\t01.txt"
>>> print(path)
c:\text\new\read\t01.txt
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data.txt")
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\\data.txt' mode='r' encoding='cp1252'>
>>> 
>>> 
>>> c = f.read()
>>> type(c)
<class 'str'>
>>> print(c)
Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too
Imagine all the people living life in peace, you

You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one

Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people sharing all the world, you

You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one
>>> f.readline()
''
>>> f.tell()
531
>>> len(c)
511
>>> f.seek(0)
0
>>> f.readline()
"Imagine there's no countries\n"
>>> f.readline()
"It isn't hard to do\n"
>>> f.readline()
'Nothing to kill or die for\n'
>>> 
>>> f.seek(0)
0
>>> c = f.readlines()
>>> c
["Imagine there's no countries\n", "It isn't hard to do\n", 'Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', '\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> type(c)
<class 'list'>
>>> 
>>> 
>>> f.seek(0)
0
>>> c = f.read()
>>> c
"Imagine there's no countries\nIt isn't hard to do\nNothing to kill or die for\nAnd no religion too\nImagine all the people living life in peace, you\n\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one\n\nImagine no possessions\nI wonder if you can\nNo need for greed or hunger\nA brotherhood of man\nImagine all the people sharing all the world, you\n\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one"
>>> 
>>> f.close()
>>> 
>>> # --------------------------------------
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "w")
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\\data2.txt' mode='w' encoding='cp1252'>
>>> f.write("Song: Imagine\n")
14
>>> f.write("Written by: John Lennon\n")
24
>>> f.write("-------------------------------------------\n\n")
45
>>> f.close()
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> c1 = ["Imagine there's no countries\n", "It isn't hard to do\n", 'Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', '\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', '\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> f.writelines(c1)
>>> f.close()
>>> 
>>> c
"Imagine there's no countries\nIt isn't hard to do\nNothing to kill or die for\nAnd no religion too\nImagine all the people living life in peace, you\n\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one\n\nImagine no possessions\nI wonder if you can\nNo need for greed or hunger\nA brotherhood of man\nImagine all the people sharing all the world, you\n\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one"
>>> 
>>> c1 = c.split()
>>> c1
['Imagine', "there's", 'no', 'countries', 'It', "isn't", 'hard', 'to', 'do', 'Nothing', 'to', 'kill', 'or', 'die', 'for', 'And', 'no', 'religion', 'too', 'Imagine', 'all', 'the', 'people', 'living', 'life', 'in', 'peace,', 'you', 'You', 'may', 'say', "I'm", 'a', 'dreamer', 'But', "I'm", 'not', 'the', 'only', 'one', 'I', 'hope', 'some', 'day', "you'll", 'join', 'us', 'And', 'the', 'world', 'will', 'be', 'as', 'one', 'Imagine', 'no', 'possessions', 'I', 'wonder', 'if', 'you', 'can', 'No', 'need', 'for', 'greed', 'or', 'hunger', 'A', 'brotherhood', 'of', 'man', 'Imagine', 'all', 'the', 'people', 'sharing', 'all', 'the', 'world,', 'you', 'You', 'may', 'say', "I'm", 'a', 'dreamer', 'But', "I'm", 'not', 'the', 'only', 'one', 'I', 'hope', 'some', 'day', "you'll", 'join', 'us', 'And', 'the', 'world', 'will', 'be', 'as', 'one']
>>> D = []
>>> D = {}
>>> for word in c1:
	if(word in D.keys()):
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'Imagine': 4, "there's": 1, 'no': 3, 'countries': 1, 'It': 1, "isn't": 1, 'hard': 1, 'to': 2, 'do': 1, 'Nothing': 1, 'kill': 1, 'or': 2, 'die': 1, 'for': 2, 'And': 3, 'religion': 1, 'too': 1, 'all': 3, 'the': 7, 'people': 2, 'living': 1, 'life': 1, 'in': 1, 'peace,': 1, 'you': 3, 'You': 2, 'may': 2, 'say': 2, "I'm": 4, 'a': 2, 'dreamer': 2, 'But': 2, 'not': 2, 'only': 2, 'one': 4, 'I': 3, 'hope': 2, 'some': 2, 'day': 2, "you'll": 2, 'join': 2, 'us': 2, 'world': 2, 'will': 2, 'be': 2, 'as': 2, 'possessions': 1, 'wonder': 1, 'if': 1, 'can': 1, 'No': 1, 'need': 1, 'greed': 1, 'hunger': 1, 'A': 1, 'brotherhood': 1, 'of': 1, 'man': 1, 'sharing': 1, 'world,': 1}
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> f.write('-'*60 + '\n')
61
>>> for key in D:
	f.write(str(key).ljust(20) + ' -----> ' + str(D[key]))

	
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> f.write('\n\n' + '-'*60 + '\n')
63
>>> for key in D:
	f.write(str(key).ljust(20) + ' -----> ' + str(D[key]))

	
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
29
>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> for key in D:
	f.write(str(key).ljust(20) + ' -----> ' + str(D[key]) + '\n')

	
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
30
>>> f.close()
>>> c
"Imagine there's no countries\nIt isn't hard to do\nNothing to kill or die for\nAnd no religion too\nImagine all the people living life in peace, you\n\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one\n\nImagine no possessions\nI wonder if you can\nNo need for greed or hunger\nA brotherhood of man\nImagine all the people sharing all the world, you\n\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one"
>>> c1
['Imagine', "there's", 'no', 'countries', 'It', "isn't", 'hard', 'to', 'do', 'Nothing', 'to', 'kill', 'or', 'die', 'for', 'And', 'no', 'religion', 'too', 'Imagine', 'all', 'the', 'people', 'living', 'life', 'in', 'peace,', 'you', 'You', 'may', 'say', "I'm", 'a', 'dreamer', 'But', "I'm", 'not', 'the', 'only', 'one', 'I', 'hope', 'some', 'day', "you'll", 'join', 'us', 'And', 'the', 'world', 'will', 'be', 'as', 'one', 'Imagine', 'no', 'possessions', 'I', 'wonder', 'if', 'you', 'can', 'No', 'need', 'for', 'greed', 'or', 'hunger', 'A', 'brotherhood', 'of', 'man', 'Imagine', 'all', 'the', 'people', 'sharing', 'all', 'the', 'world,', 'you', 'You', 'may', 'say', "I'm", 'a', 'dreamer', 'But', "I'm", 'not', 'the', 'only', 'one', 'I', 'hope', 'some', 'day', "you'll", 'join', 'us', 'And', 'the', 'world', 'will', 'be', 'as', 'one']
>>> 'you\'ll'
"you'll"
>>> f1 = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> f2 = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\data2.txt", "a")
>>> f1
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\\data2.txt' mode='a' encoding='cp1252'>
>>> f2
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\\data2.txt' mode='a' encoding='cp1252'>
>>> 
