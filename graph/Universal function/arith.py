import numpy as m
x=m.arange(5)
y=m.arange(5)

print("X= ",x)
print("Y= ",y)

newarr=m.add(x,y)
print("addition = ",newarr)
newarr=m.subtract(x,y)
print("subtraction = ",newarr)
newarr=m.multiply(x,y)
print("addition = ",newarr)
try:
    newarr=m.divide(x,y)
except ZeroDivisionError as d:
    print("division by zero is not possible")  
else:      
   print("division = ",newarr)