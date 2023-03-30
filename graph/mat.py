import matplotlib.pyplot as pl
import numpy as np

x=np.array([0,6])
y=np.array([0,250])

p1=[1,10,91,100]
p2=[12,41,-100,10]

#linestyle=ls
#solid,dashdot,dotted,

#marker
font={"family":"arial",'color':'blue','size':15}
pl.xlabel("x-axis")
pl.ylabel("y-axis")
pl.title("stats graph",fontdict=font,loc='left')
pl.plot(p1,p2,'D',ls="dashdot")
pl.show()