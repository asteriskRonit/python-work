import matplotlib.pyplot as plt
n=int(input("Enter the number "))
lst=[]
while n!=1:
    if n%2!=0:
        n=n*3+1
    else:
        n/=2
    lst.append(n)    
    print(n,end="  ")        

print()
print("The sequence is ",lst)
plt.plot(lst)
plt.show()
