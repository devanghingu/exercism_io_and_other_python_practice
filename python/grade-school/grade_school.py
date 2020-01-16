class School:
    def __init__(self):
        self.dict={}

    def add_student(self, name, grade):
        self.dict[name]=grade
    def roster(self):
        newlist=sorted(self.dict.items() ,key=lambda newlist: newlist[1])
        return  [i[0] for i in sorted(newlist,key= lambda p:(p[1],p[0]))] 
        
        
    def grade(self, gno):
        return sorted([i for i in self.dict if (self.dict[i]==gno)])
            
                
# school = School()
# school.add_student(name="Peter", grade=2)
# school.add_student(name="Anna", grade=1)
# school.add_student(name="Barb", grade=1)
# school.add_student(name="Zoe", grade=2)
# school.add_student(name="Alex", grade=2)
# school.add_student(name="Jim", grade=3)
# school.add_student(name="Charlie", grade=1)
# print(school.roster())