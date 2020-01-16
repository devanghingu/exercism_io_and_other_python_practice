def is_armstrong_number(number):
    no,newno,leng=number,0,len(str(number))
    if (number == 0):
        return True
    while no>0:
        lno=int(no%10)
        newno=int(newno + (lno**leng))
        no=int(no/10)
    if newno == number:
        return True
    else:
        return False