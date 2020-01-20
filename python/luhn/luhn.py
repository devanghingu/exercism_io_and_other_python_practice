class Luhn:
    def __init__(self, card_num):
        # card_num="".join(card_num.split(" "or'\-'))
        self.card_num=card_num
        self.new_no=card_num
        print(self.card_num)
    def valid(self):
        for i in range (0,len(self.card_num),2):
            doubleno=int(self.card_num[i])**2
            if doubleno >9:
                doubleno-=9
            self.new_no.insert(i,doubleno)
            
        print("old no",self.card_num)
        print("new no",self.new_no)
        if sum(self.new_no)% 10 ==0:
            return True
        else:
            return False
l=Luhn("055444285")
l.valid()
