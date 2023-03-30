class A:
   def __init__(self):
      print("hello the class obj has been initialized")
   def print_name(self):
       print("my name is dash")  

class B:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def sum(self):
        print("the addittion of number is ",self.first+self.second)       

class C:
    def onsert(self,number):
        self.no=number
    def thenumber(self):
        print("The number is ",self.no)               

er=A()
er.print_name()

maths=B(10,21)
maths.sum()

key=C()
key.onsert(101)
key.thenumber()