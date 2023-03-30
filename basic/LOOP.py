m=0
while(m<=3):
    print("The value and id is ",m,hex(id(m)))
    m+=1
k=0   
print("The value and id is ",k,hex(id(k)))
  
for i in range(0,10):
    print(i,end=" ")
print()
print("out of loop ",i)

for x in range(0,5):
    for y in range(0,x+1):
        print("*",end=" ")
    print()  
lo=["VTUEEE","paul","ronit"]      
for i in range(len(lo)-1,-1,-1):
    if lo[i]=="ronit":
        continue
    print(lo[i],end=" ")
print()
stro="ronit paul"
print("length of the string",len(stro))
for b in stro:
    print(b,end="")    
print()
#iterator
itu=iter(stro)
print(next(itu))    
print(next(itu))
