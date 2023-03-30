tyuple=("here","hello","world")
print(type(tyuple))
print(tyuple)
for i in tyuple:
    print(i)
for x in range(len(tyuple)-1,-1,-1):
    print(tyuple[x]) 

tiu=("ronit")*3+("paul")*2
print(tiu)       

lis=[1,"ronit","paul"]
ty=tuple(lis)
tyy=ty[::-1]

#del tyy
print(tyy)