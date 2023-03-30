class node:
    def __init__(self,number):
        self.value=number
        self.left=None
        self.right=None
    def traversing(self):
        print(self.value,end="  ")
        if self.left:
            self.left.traversing()
        if self.right:
            self.right.traversing()



root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.traversing()
