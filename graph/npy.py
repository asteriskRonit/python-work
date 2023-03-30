def printval(deco):
    print("TYPE =",deco.dtype," VALUE =",deco)
import numpy as np
arr=np.array([10,11,12,13])
arr1=np.array([[10,11,12,13],[10,11,12,13]])
print(arr.ndim,arr1.ndim)
print(arr)
print(type(arr))

are=np.array(["abcd",2,3])
print(are.dtype)

ar=np.array([1,2,3],dtype='S')
print(ar.dtype)

krk=np.array([1.2,2.33,3.1])
printval(krk)
new=krk.astype('i')
printval(new)