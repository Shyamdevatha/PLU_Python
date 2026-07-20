class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class Tree_structure:
    def __init__(self,data):
        self.root = None
        
    def create_root(self,data):
        self.root = Node(data)
        return self.root
    
    def insert_node(self, data): 
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(data, self.root)
            
    def _insert_node(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_node(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_node(data, current_node.right)
        else:
            # If the data is equal, we do not insert duplicates
            pass
        
    
# object of the class tree_structure 
node= Tree_structure(10)

# root node of the tree
root = node.create_root(10)

node1 = node.insert_node(5)
node2 = node.insert_node(15)