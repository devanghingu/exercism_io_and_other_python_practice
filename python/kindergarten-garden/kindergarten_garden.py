import string
class Garden:
    def __init__(self, diagram, students=""):
        self.alapha=string.ascii_lowercase[:] # get all alphabatic character
        self.allplants=['Grass', 'Clover', 'Radishes','Violets']
        self.diagram=diagram.split('\n') # splitted plant 
        if students!="":
            self.students=sorted(students)
        else:
            self.students=""
    def plants(self,student):
        if self.students == "":
            position=self.alapha.index(student[0].lower())+1
            return self.getplants(position)
        else:
            position=self.students.index(student)+1
            return self.getplants(position)
    def getplants(self,position):
        total_plant=[]
        position=(position*2)-1
        pattern=self.diagram[0][position-1:position+1]
        pattern+=self.diagram[1][position-1:position+1]
        for char in pattern:
            total_plant+=[plant for plant in self.allplants if plant[0] in char]
        return total_plant



# ga=Garden('ABCDEFGHIJKLLMNOPQRSTUVWXYZ\ABCDEFGHIJKLLMNOPQRSTUVWXYZ')

ga=Garden('VVCCGG\nVVCCGG')
print(ga.plants('Charlie'))
#  1a    2b    3c    4d    5e    6f   7g
# 0 1 | 2 3 | 4 5 | 6 7 | 8 9 |10 11|12 13|
# 123456789
#[dcvfdcvfdc]
#[dcvfdcvfdc]

# a1 0:2
# b2 2:4
# c3 4:6
# d4 6:8
# e5 8:10





