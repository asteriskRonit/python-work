import numpy as np
#n=int(input("Number of elemnts u want: "))
#arra=np.array([float(input("Enter the number: ")) for x in range(n)])
arra=np.array([-1,2,44,1,21,-2,11,12,0])
dict={}
print(arra)
arra=np.sort(arra)
print(arra)
print(-1 in dict.keys())
for i in range(1,len(arra)):
    if arra[i-1]==arra[i]:
        print(arra[i-1],arra[i])
        if arra[i] in dict.keys():
            dict[arra[i]]+=1
        else:
            dict[arra[i]]=1    

if len(dict)>0:
    print("The duplicate list is : ",dict)
else:
    print("there is no duplicate element")    