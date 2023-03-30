import numpy as n
x=n.random.uniform(1,7,5)
y=n.random.uniform(5,10,5)
z=[]
k=[]
print(x,y)

for i,j in zip(x,y):
    z.append(i+j)
print(z)

k=n.add(x,y)
print(k)


