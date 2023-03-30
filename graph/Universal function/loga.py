import numpy as n
arr=n.arange(1,10)
print("logarithmic of base 2 = ",n.log2(arr))
print("logarithmic of base 10 = ",n.log10(arr))
print("Natural logarithmic = ",n.log(arr))
#sumation of the element
arr1=n.array([1,4,10,45])
arr2=n.array([3,5,8,9])
X=n.sum([arr1,arr2],axis=1)
print(X)
Y=n.cumsum(arr2)
print(Y)
