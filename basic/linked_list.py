class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.data)
            printval=printval.next    
    
class test:
    head=10

pi=linkedList()
pi.headval=node("ronit")
e1=node("hash")
e3=node("hashing")

pi.headval.next=e1
e1.next=e3

pi.listprint()

e2=test()
e2.head=21
print(e2.head)


