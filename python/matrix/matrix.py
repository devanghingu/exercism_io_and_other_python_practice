class Matrix:
    def __init__(self, matrix_string):
        #first split through \n
        self.matrix_string=matrix_string.split('\n')
        
        #define matrix data to store all data
        self.matrix_data=[]
        
        #now split using space so i will appne into two dim array 
        for i in self.matrix_string:
            self.matrix_data.append(i.split(' '))
        #convert str to int 
        
        for i in range(len(self.matrix_data)):
            list1=[]
            list1=[int(j) for j in self.matrix_data[i]]
            self.matrix_data[i]=list1
    
    def row(self, index):
        return self.matrix_data[index-1]

    def column(self, index):
        #prepare column
        list1=[]
        for i in self.matrix_data:
            list1.append(i[index-1])
        return list1
