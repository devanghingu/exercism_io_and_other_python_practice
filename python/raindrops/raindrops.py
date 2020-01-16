def convert(no):
    result=""
    if(no% 3==0):
        result+="Pling"
    if(no% 5==0):
        result+="Plang"
    if (no% 7==0):
        result+="Plong"
    if(result==""):
        result=str(no)
    return result
        