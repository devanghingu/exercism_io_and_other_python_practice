def is_isogram(data):
    data=data.lower() #first make string in lower
    
    setdata=[i for i in set(list(data)) if i!= ' ' and i!='-']
    listdata=[i for i in list(data) if i!= ' ' and i!='-']
    if(len(setdata) != len(listdata)):
        return False
    return True
# print(is_isogram('devang'))