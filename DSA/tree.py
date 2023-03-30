class Tree_node:
    def __init__(self, data):
          self.data=data
          self.left=None
          self.right=None    

def pre_traversal(Node):
     if Node!=None:
            print(Node.data)
            pre_traversal(Node.left)
            pre_traversal(Node.right)

n1=Tree_node(10)
n2=Tree_node(2)
n3=Tree_node(11)

n1.left=n2
n1.right=n3

pre_traversal(n1)
