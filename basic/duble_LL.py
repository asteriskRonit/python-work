class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class LL:
    def __init__(self):
        self.headvalue=None

def lastnode(value):
      while value.next is not None:
        value=value.next

      return value  


lk=LL()
lk.headvalue=Node("ronit")
lk2=Node("paul")
lk3=Node("computer science")
lk2.previous=lk
lk.next=lk2
lk2.next=lk3
lk3.previous=lk2

tt=lastnode(lk.headvalue)
print("The value {} done".format(tt.data))





