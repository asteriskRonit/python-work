from threading import Thread
import threading
arr=[]
def take_input(n):
    global arr
    arr=[int(input("Enter the values: ")) for z in range(n)]
    print("The array is : ",arr)

def sum_ation():
    k=0
    for i in arr:
        k+=i
    print()    
    print("The value of the sumation : ",k)

x=lambda a:a*10
print(x(10))
t1=threading.Thread(target=take_input,args=(2,))
t1.start()
t1.join()
t2=threading.Thread(target=sum_ation)
t2.start()
t2.join()
