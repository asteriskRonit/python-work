import threading
import time
def square_no(no):
    print(no*no)
   
    print("complete")

t1=time.time()
t1=threading.Thread(target=square_no,args=(10,))
t1.start()
t1.join()
print("hello")
print("tq")
print(time.time())

