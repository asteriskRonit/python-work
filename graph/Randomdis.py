from numpy import *
arra=random.choice([2,1,3,4],p=[0.2,0.3,0.3,0.2],size=(100))
arra2=random.choice([1,2,3,4],p=[0.2,0.3,0.3,0.2],size=(3,5))
print(arra)
print(arra2)
#permutation
ara=array([21,33,44,55])
random.shuffle(ara)
print(ara)
print(random.permutation(ara))