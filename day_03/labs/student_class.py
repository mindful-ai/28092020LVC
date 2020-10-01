class student(object):

    # Class Variables
    nstudents = 0
    schoolname = ''

    # Data/attributes
    def __init__(self, name, c, rid):
        print('Initializing values.....')
        self.name   = name
        self.cls    = c
        self.regid  = rid
        self.math   = 0
        self.phy    = 0
        self.chem   = 0
        self.bio    = 0
        self.avg    = 0
        student.nstudents += 1

    # Special functions

    def __str__(self):   # This makes the class and its objects compatible with print()
        return self.name + '\\' + str(self.cls) + '\\' + self.regid

    def __repr__(self):
        return 'student' + '.' + self.name
        
    # Functions/methods

    def setschoolname(self, schoolname):
        student.schoolname = schoolname

    def printinfo(self):
        self.state = 'Karnataka'
        print('STATE : ', self.state)
        print('SCHOOL: ', student.schoolname)
        print('-----------------------------------')
        print('NAME: ', self.name)
        print('CLASS: ', self.cls)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.math)
        print('PHYSICS  : ', self.phy)
        print('CHEMISTRY: ', self.chem)
        print('BIOLOGY  : ', self.bio)
        print('-----------------------------------')
        print('AVERAGE  : ', self.avg)
        print('NSTUDENTS  ------> ', student.nstudents)
        print('\n')

    def setMaths(self, marks):
        self.math = marks

    def setPhysics(self, marks):
        self.phy = marks

    def setChemistry(self, marks):
        self.chem = marks

    def setBiology(self, marks):
        self.bio = marks

    def calcAverage(self):
        self.avg = (self.phy + self.chem + self.math + self.bio) / 4

# ------------------------------------------------------

if __name__ == '__main__':

    s = student('Ram', 5, 'CL001')
    s.printinfo()

    s.setschoolname('Kendriya Vidyalaya')
    s.setBiology(90)
    s.setChemistry(98)
    s.setPhysics(95)
    s.setMaths(100)
    s.printinfo()

    s.calcAverage()
    s.printinfo()
