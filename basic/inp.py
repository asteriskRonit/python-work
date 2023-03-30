LST=[]
n=int(input("enter the number of items in the list: "))
for i in range(0,n):
    el=input()
    LST.append(el)

print(LST)

for x in range(0,len(LST)):
    print(type(LST[x]))

tup=("nyc","del","kol")
lk=list(tup)
print(lk)

