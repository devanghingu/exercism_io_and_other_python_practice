def classify(number):
    if(number <= 0):
        raise ValueError('number should not be in nagative or zero')
    # data=sum([i for i in range(1,number) if(number % i == 0)])
    data=sum(filter(lambda a : (number % a == 0),list(range(1,number))))
    if (data==number):
        return "perfect"
    elif (data>number):
        return "abundant"
    return "deficient"


# print(classify(6))    

sdlfjksf
