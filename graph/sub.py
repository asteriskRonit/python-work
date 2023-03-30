import matplotlib.pyplot as ppo
import os
'''n=int(input("enter the number of points : "))
x=[int(input("enter the points of x-axis : ")) for x in range(0,n)]
print()
y=[int(input("enter the points of y-axis : ")) for x in range(0,n)]
print()
os.system('CLS')
print(x,y)'''

x=[1,2,3]
y=[-1,-11,-22]
ppo.subplot(2,1,2)
ppo.plot(x,y,"D",ls="dotted")

x=[11,12,13]
y=[1,11,22]
ppo.subplot(2,1,1)
ppo.plot(x,y,"o",ls="dashdot")

#ppo.plot(x,y,'o',ls='dashdot')
ppo.title("subplot graph")
ppo.show()

