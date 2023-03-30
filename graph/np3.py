#concat
import numpy as df
arr1=df.array([1,2,3])
arr2=df.array([11,22,33])
arr=df.concatenate((arr1,arr2))
arrr=df.stack((arr1,arr2),axis=1)
arrry=df.hstack((arr1,arr2))
arrryy=df.vstack((arr1,arr2))
arrryyy=df.dstack((arr1,arr2))
print(arr)
print(arrr)
print(arrry)
print(arrryy)
print(arrryyy)



