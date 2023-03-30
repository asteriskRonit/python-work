class Abs:
    _protected=22
    __private=11

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
         print("this is from repr method")
         return ("a : %s  b : %s" % (self.a,self.b))

    def __str__(self):
         print("this is from str method")
         return ("a : %s  b : %s" % (self.a,self.b))     

obj=Abs()
print("calling the private method from outside ",obj._Abs__private)    
print("calling the protected method from outside ",obj._protected)    

obj2=Test(21,2)
print(obj2)
print([obj2])