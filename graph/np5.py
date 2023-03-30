from numpy import random
class dfg:
    pblic=10
    _prtcd=11
    __prvt=21


std=dfg()
print("public= ",std.pblic,"protected= ",std._prtcd,"private= ",std._dfg__prvt)    

#random specimens
x=random.randint(2)
y=random.rand(2)
#random 1D array
arr=random.randint(2,size=(5))
#random 2-D arrayy
arr2=random.rand(3,5)
print(x,y)
print(arr)
print(arr2)

k=random.choice([1,11,23,41],size=(3,5))
print(k)