import numpy as np
def mysub(x,y):
    return x-y

x=np.random.uniform(1,7,5)
y=np.random.uniform(5,10,5)
print("X = ",x)
print("Y = ",y)
ysub=np.frompyfunc(mysub,2,1)
print(ysub(x,y))
print(type(np.yy))
