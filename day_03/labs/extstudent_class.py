from student_class import student

class extstudent(student):

    # Attributes
    def __init__(self, name, c, rid, native='Earth', extra=['music']):
        super().__init__(name, c, rid)
        self.native = native
        self.extra = extra

    # Functions
    def getGrade(self): # New function in the extended class
        if(self.avg > 90):
            return 'A+'
        elif(70 < self.avg <= 90):
            return 'A'
        elif(50 < self.avg <= 70):
            return 'B'
        else:
            return 'C'

    def printinfo(self):  # Overriding the function
        super().printinfo()
        print('-----------------------------------')
        print('GRADE  : ', self.getGrade())
        print('NATIVE : ', self.native)
        print('EXTRAS : ', self.extra)
        print('\n\n')
    

if __name__ == '__main__':

    # -------------------------------------------- Backward compatibility test

    '''
    s = extstudent('Ram', 5, 'CL001')
    
    
    s.printinfo()

    s.setschoolname('Kendriya Vidyalaya')
    s.setBiology(90)
    s.setChemistry(98)
    s.setPhysics(95)
    s.setMaths(100)
    s.printinfo()

    s.calcAverage()
    s.printinfo()

    '''

    # ----------------------------------------------------------------------------

    s = extstudent('Ram', 5, 'CL001', 'J P Nagar, Bangalore', ['music', 'travel', 'swimming'])
    
    
    s.printinfo()

    s.setschoolname('Kendriya Vidyalaya')
    s.setBiology(90)
    s.setChemistry(98)
    s.setPhysics(95)
    s.setMaths(100)
    s.printinfo()

    s.calcAverage()
    s.printinfo()


    # --------------------- Polymorphism

    s1 = student('Kiran', 5, 'CL002')
    s1.setschoolname('Kendriya Vidyalaya')
    s1.setBiology(95)
    s1.setChemistry(92)
    s1.setPhysics(91)
    s1.setMaths(99)
    s1.calcAverage()


    # ------------------------ study the behavior here
    
    print('-------------- POLYMORPHISM')

    # Backend
    x = s1
    #x = s
    
    # Frontend
    x.printinfo()
    