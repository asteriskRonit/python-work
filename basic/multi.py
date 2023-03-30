from threading import *
import threading
from time import sleep
class hello(Thread):
   def run(self):
    for i in range(50):
        print("hello")
        sleep(0.1)

class hi(Thread):
    def kept(self):
        for i in range(50):
            print("hI")
            sleep(0.1)

def age(n):
    print("ypur age is ",n)

T1=hello()
T2=hi()

T1.start()
T2.start()

p1=threading.Thread(target=age,args=(10))
p1.start()
print("Thank u")