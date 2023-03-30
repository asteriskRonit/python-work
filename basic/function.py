def myname(fname,lname):
    print("my name is ",fname,"",lname)

def info(*student):
    print(student)
    print(type(student))

def numbers(fn,ln):
    print(fn,ln)

def numbers(aj,b):
    print("hello there")

def list_add(listy,add):
    lll=list(listy)
    lll.append(add)
    return lll
                     
def number_l(**kwrd):
    print(kwrd["f"],kwrd["e"],kwrd['b'])    

myname("ronit","paul")   
info(1,2,3,4) 
info([1,2,3,6])
ll=[1,2,3]
ll=list_add(ll,10)
print(ll)
numbers(10,11)
number_l(f=10,e=11,b=320)

x=lambda a:a**2
print("the lambda function:: ",x(3))

y=lambda z,x:z if z>x else x
print("the grater value ",y(int(input("Enter the first value: ")),int(input("Enter the second value: "))))
  