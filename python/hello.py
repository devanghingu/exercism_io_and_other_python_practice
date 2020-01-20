# def hello_string(abc :str) -> str:
#     return True

# print(type(hello_string("hello world")))

# argswithlam=lambda *args,**ab: print(ab)
# a={}
# # a["asdf"]='asdf'
# m={'a': 2, 'b': 1}
# n=(lambda *x,**y: sum(x+tuple(y.values())))
# # print(n(m.values()))
# print(n(1, 2, 3,a=1,b=2))
#----------delete attribute----------
# class Myclass:
#     def hello(self):
#         print('hello')
#     def __init__(self):
#         # super().__init__()
#         self.abc='a'
#     def __delattr__(self, name):
#         self.__dict__[name]
#         print("deleted")
#         # return self.__delattr__(name)
    
# ob=Myclass()
# ob.hello()
# del ob.abc
#-------operator overloading-------
# class Addition:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return ("{},{}".format(self.x,self.y))
#     def __sub__(self,addobj):
#         x=self.x+addobj.x
#         y=self.y+addobj.y
#         return Addition(x,y)
#     def __len__(self):
#         return 5
# one=Addition(5,4)
# two=Addition(4,5)
# print(one-two)
# print(one.__len__())
#------iter
# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""

#     def __init__(self, max = 0):
#         self.max = max

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
        