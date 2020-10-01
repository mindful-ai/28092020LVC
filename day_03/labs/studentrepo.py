from extstudent_class import extstudent

# ------------------------------------------- Step 1

f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\code\case\student.txt", "r")
content = f.readlines()
f.close()

# ------------------------------------------- Step 2

studobjs = []

coldata = content[0]
columns = [item.strip() for item in coldata.split(',')]
for rowdata in content[1:]:
    rows = [item.strip() for item in rowdata.split(',')]
    sd = dict(zip(columns, rows))
    s = extstudent(sd['name'], 7, sd['regid'])
    s.setschoolname('Kendriya Vidyalaya')
    s.setBiology(float(sd['bio']))
    s.setChemistry(float(sd['chem']))
    s.setPhysics(float(sd['phy']))
    s.setMaths(float(sd['math']))
    studobjs.append(s)


# ------------------------------------------- Step 2

'''
for obj in studobjs:
    obj.calcAverage()
    obj.printinfo()
'''

# --------------------------------------------------- FRONT END

studname = input('Enter name: ')
for obj in studobjs:
    if(obj.name == studname):
        obj.printinfo()

