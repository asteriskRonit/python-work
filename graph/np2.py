import numpy as np
arr=np.array([11,112,321])
new=arr.copy()
new[0]=69
print(new)
print(arr)

now=arr.view()
now[0]=69
print(new)
print(arr)

print(new.base)
print(now.base)

arra2=np.array([[1,2,3,4],[10,11,12,1]])
print(arra2.shape)
are=np.array([1,23,33],ndmin=3)
print(are.shape)