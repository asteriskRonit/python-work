for i in range(1,6):
    for x in range(0,i):
        if i>2 and (x!=0 and x!=i-1):
            print(i-1,end=" ")
        else:    
            print("1",end=" ")
    print()     