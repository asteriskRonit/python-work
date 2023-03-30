import single


lost = single.list
while(lost.nextval!=None):
    print(lost.nextval.dataval, end=" ")
    lost = lost.nextval
print(" ")

