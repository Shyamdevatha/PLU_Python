'''
Stack 
'''
# from collections import deque

# stack_container = deque()


# var = input("Enter the value : ")
# stack_container.append(var)
    
# stack_container.pop()

# var= stack_container.pop(<value>)


# tree 
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None 
        self.data = data 


class TreeStructure:
    def createRoot(self,data):
        self.root = Node(data)
        
    def insertNode(self,data):
        self.new_node = Node(data)
        
        # logic 1 
        if self.root.left == None : 
            self.root.left = self.new_node
        elif self.root.right == None:
            self.root.right= self.new_node
        else : 
            print(" move to the next level as the root is connected to two nodes ")
            
        # Approach two 
        
    def left(self, root_node,node):
        self.root.left = self.node
    def right(self, root_node,node):
        self.root.right = self.node
        
    def move_to_next(self, node):
        next_node = 0
        if node.left:
            return next_node = node.left
        else: 
            return next_node = node.right