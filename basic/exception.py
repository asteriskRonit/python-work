def function_lev(leb):
    if leb < 0:
        raise "Invalid no", leb
a=10
b=10
try:
    c=a/b
except ZeroDivisionError as d:
    print("divide by zero ",d)
else:
    print("THE VALUE OF THE DIVISION IS ",c)  
finally:
    print("system is closed")    

if a is b:
    print("same value")

try:
    function_lev(0)
except Exception as a:
    print("problem on number")



