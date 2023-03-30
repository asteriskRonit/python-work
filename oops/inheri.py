class maths:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class add(maths):
   def sum(self):
    return self.a+self.b

class subtract(maths):
    def sub(self):
        return self.a-self.b

#driver code

'''ad=subtract(10,7)
print("the additio of the value is ",ad.sum())         
print("the subtractin of the value is ",ad.sub()) '''        

class A(object):
    def __init__(self) :
       print("hello form class A")
       self.str1="ronit"
class B(object):
    def __init__(self):
       print("hello from class B")
       self.str2="paul"
class C(A,B): 
    def __init__(self):
       A.__init__(self)
       B.__init__(self)
       print("hello from dreived class")
    def printstrs(self):
        print(self.str1,self.str2)  

d=C()
d.printstrs()







