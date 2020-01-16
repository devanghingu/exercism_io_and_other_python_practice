import re
def abbreviate(words):
    # words=words.split('_')
    words=re.sub("[_-]"," ",words).upper().strip().split()
    return "".join([i[0].upper() for i in words])        
print(abbreviate("Hingu _devang_ ra"))