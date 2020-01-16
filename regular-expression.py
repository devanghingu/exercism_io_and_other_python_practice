import re
from re import split
    txt="this is my string and this not more you 'complex', String, which you're thinking complex.!@#$%^".lower()
test=re.compile(" '.*' ")

# print(test.findall(txt)) #find '' in string 
# print(test.match)

print(split('\W+', txt)) 