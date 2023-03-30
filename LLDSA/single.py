def printing():
    print("we are inside the class")

class Node:
   def __init__(self, data=None):
      self.dataval = data
      self.nextval = None


   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = Node()
e1=Node(1)
e2 = Node(3)
e3 = Node(4)

# Link first Node to second node
list.nextval = e1

# Link second Node to third node
e1.nextval = e2
e2.nextval=e3
lost=list
while(lost.nextval!=None):
    print(lost.nextval.dataval, end=" ")
    lost = lost.nextval
print(" ")

no = int(input("Enter the no you want to insert: "))
user = Node(no)
lost = list
ind = int(input("Enter the number you want to insert before that "))
while(lost.nextval.dataval!=ind):
    lost = lost.nextval
swap = lost.nextval
lost.nextval = user
user.nextval = swap