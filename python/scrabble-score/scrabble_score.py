def score(word):
    text={}
    text['A''E''I''O''U''L''N''R''S''T']=1
    text['D''G']=2
    text['B''C''M''P']=3
    text['F''H''V''W''Y']=4
    text['K']=5
    text['J''X']=8
    text['Q''Z']=10
    totalscore=0
    for i in word.upper():
        totalscore+=sum(list([val for arr,val in text.items() if i in arr]))
    return totalscore
