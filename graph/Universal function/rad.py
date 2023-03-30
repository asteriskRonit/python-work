import numpy as n
arr=n.array([90,180,270])
x=n.deg2rad(arr)
print(x)

rad=n.array([n.pi/2,n.pi,1.5*n.pi,2*n.pi])
y=n.rad2deg(rad)
print(y)

#finding angles
angle=n.arcsin(1.0)
print(angle)