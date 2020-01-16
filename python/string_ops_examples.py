#!/usr/bin/python3

data=" Praesent fermentum augue et ligula imperdiet, ut condimentum metus ornare. Pellentesque eu diam elit."
# capatilize function,casefold remained 
print("data in capatalize   \n\t\t",data.capitalize())

#replcace underscore(_) instead of space
print("space replaced by (_) \n\t\t",data.replace(' ',''))

#find function have thee param search keyword, start, end position
print("find i's lower position is: ",data.find('i'))
#count number of 'P' in string 
print("there are following number of 'p' in String\n", data.lower().count('p'))

#center data in whole string
print("hello world!".capitalize().center(50,"*"))

#format function 
print("1+2 is {0}.".format(3))