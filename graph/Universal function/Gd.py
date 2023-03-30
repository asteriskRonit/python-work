import numpy as n
def hello():
    def red():
        print("hello from inner function")
    red()
    print("hello from outside")    

hello()

number1=10
number2=11

no_arr=n.arange(1,5)

x=n.lcm(number1,number2)
xy=n.gcd(number1,number2)
y=n.lcm.reduce(no_arr)
yx=n.gcd.reduce(no_arr)
print("Lowest common multiplier : ")
print(x,y)

print("Highest common factor || greatest common denominator")
print(xy,yx)


