import threading
def hello(n):
    for i in range(5):
        print("hello")

def hy():
    for i in range(5):
         print("hy")       
         
t1=threading.Thread(target=hello,args=(10,))       
t2=threading.Thread(target=hy)      
t2.start() 
t1.start()  
t1.join()