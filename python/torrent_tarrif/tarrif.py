class Tarrif:
    """Tarrif class(for Torrent power) for get energy consumption  
        all input from user and make calculation according to input."""
    def __init__(self):
        self.all_cat,self.bill=['rgp','glp','non-rgp','ltp-ag','sl','ltp','ltp-ag','lev','lev-lt','tmp'],0
        print("_"*60)
        while True:
            print('Category Name must be saparated by "- (Hyphan-Sign)" ')
            category="-".join(input("Enter Category:- ").split('-')).lower()
            category="-".join(category.split(' ')).lower()
            if category in self.all_cat:
                self.category=category
                break
            else :
                print("Envalid category name try again")
                continue
        #category init done 
        print("_"*60)
        self.unit=int(input("Enter Number Of Unit:- "))
        # if(self.category in ['rgp','gpl'])
    def init_phasetype(self):
        print("_"*60)
        self.phase_type=input('Phase type (Single-Phase | Three-Phase )=>[S/T]:- ').lower()
        return self.phase_type
    
    def init_kw(self):
        print('enter power capacity in KW 5_to_15 ')
        print('_'*60)
        self.kw=int(input("Enter Rated Watts in 'KW':- "))
        return self.kw
    def init_bhp(self):
        print('_'*60)
        self.bhp=int(input('Enter Break HorsePower(BHP) in digit: '))       
        return self.bhp
    def make_calculation_4(self):
        print(self.unit)
        if self.category == 'rgp':
            self.init_phasetype()
            print("_"*60)
            print('\nSelect "Below Poverty Line" | "Residential General Purpose" ')
            self.subcat=input('B or BPL for-> BPL \t & \t R or RGP for -> RGP:- ').lower()
            if self.subcat[0] == 'r': #RGP
                unit=self.unit #{50:320,150:390}
                if unit<=50:
                    self.bill+= (unit * 320)
                elif unit<=200:
                    self.bill+=(50*320)+ ((unit-50)*390)
                else: #166
                    self.bill+= (50*320) + (150*390) + ((unit-200) * 490)
                self.bill/=100
                self.bill+= 25 if self.phase_type[0] =='s' else 65
            elif self.subcat[0] == 'b': #BPL
                self.bill=5 # fix charges direcly added  RS-5 ]
                unit=self.unit 
                if unit<=30:
                    self.bill+=(unit*150)
                elif unit<=50:
                    self.bill+= (30*150) + ((unit-30) * 320)
                elif unit<=200:
                    self.bill+= (30*150) + (20*320) + ((unit-50) * 390)
                else:
                    self.bill+= (30*150) + (20*320) + (150*390) + ((unit-200) * 490)
                # {30:150,20:320,150:390}
                self.bill/=100
        elif self.category == 'glp':
            self.init_phasetype()
            self.bill=0
            unit=self.unit
            if unit <=200:
                self.bill+=(unit*410)/100
            else:
                self.bill+=((200*410)+ ((unit-200)*480))/100
            self.bill+= (30 if self.phase_type[0] == 's' else 70)
        elif self.category == 'non-rgp':
            self.bill= (self.unit*450)/100
            while True:
                self.init_kw()
                if self.kw <= 5:
                    self.bill+=70
                    break
                elif (self.kw > 5) and(self.kw <=15):
                    self.bill+=90
                    break
                else:
                    print('envalid KW entered in NON-RGP')
                    continue
        elif self.category =='sl':
            self.bill=(self.unit*420)/100
        elif self.category in ['ltp', 'ltp-ag']:
            self.bill=((unit*330)/100) + (self.init_bhp()*10)
        elif self.category in ['lev','lev-lt']:
            self.bill=((self.unit*410)/100) + 25 
        elif self.category in ['tmp']:
            self.bill=((self.unit *500)/100) + (self.init_kw()*25)
    
    def print_bill(self):
        print("_"*60)
        print("your bill is ",self.bill)
        
obj1=Tarrif()
obj1.make_calculation_4()
obj1.print_bill()