from math import sqrt
def prime(N):
    num=1
    count=0
    try:
        if N == 0:
            raise ValueError("ValueError exception thrown {0}".format(N))
        while(True):
            num=num+1
            if checkprime(num):
                count=count+1
            if count==N:
                return num
                break
    except Exception as e:
        raise ValueError("ValueError ")


def checkprime(num):
    try:
        sqroot=int(sqrt(num))
        j=2
        while j<=sqroot:
            if num%j==0:
                return False
            j=j+1
        return True
    except Exception:
        raise ValueError("ValueError exception thrown")
