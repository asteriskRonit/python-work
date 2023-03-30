class Poly:
    def craw(self,a):
        print("done done from poly")

class coly(Poly):
    def __init__(self):
        print("hello from coly constructor")   

class lambo:
    def origin(self):
        print("it is originated from italy")
    def dimension(slef):
        print("length : {}  width : {}  height : {}".format(4000,2000,1000))  
    def seater(slef):
        print("it is 2 seater car")      
    def price(self):
        print("the price of lambo started from $3M")    
class porshe(lambo):
    def dimension(slef):
        print("length : {}  width : {}  height : {}".format(4200,1900,1000))  
    def seater(slef):
        print("it is 4 seater car")      
    def price(self):
        print("the price of lambo started from $1M")    

def func(obj):
    obj.origin()
    obj.dimension()
    obj.seater()
    obj.price()

oj=coly()
oj.craw(10)

ott=porshe()
func(ott)



