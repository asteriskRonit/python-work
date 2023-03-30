import numpy as np
#sort
arr=np.array([0,1,3,-1,2,11,7])
print(np.sort(arr))
arr2=np.array(["tupla","tuple","ball","egg"])
print(np.sort(arr2))
ar3=np.array([True,False,True])
print(np.sort(ar3))

#ait=np.array([int(input("Enter the number: ")) for x in range(0,2)])
#print(ait)

#filter
arrat=np.array([68,102,89,69,70])
filter_arr=[]
for i in arrat:
    if i%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr=arrat[filter_arr]
print(new_arr)            

#search
nre=np.array([1,2,11,23,44,11])
nre=np.sort(nre)
X=np.where(nre==11)
print("type=",type(X)," value=",X)