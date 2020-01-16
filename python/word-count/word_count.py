import re
def count_words(sentence):    
    data=re.sub("[^\w ']| '|' |'[^\w]|_|'$"," ",sentence).lower().strip().split()
    return {i:data.count(i) for i in data}
# txt="this is my string and this :not more: you 'complex'!!, String, which you're thinking complex.!@#$%^".lower()
# count_words(txt)