class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    # creating the root node of the binary tree
    def __init__(self, data):
        self.root = Node(data)
        
    def insertNode(self, data):
        NewNode = Node(data)
        if self.root is None:
            self.root = NewNode
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = NewNode
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = NewNode
                        break
                    else:
                        current = current.right
                        
    def deleteNode(self, data):
        self.root = self._delete_rec(self.root, data)
    
    def _delete_rec(self, node, data):
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_rec(node.left, data)
        elif data > node.data:
            node.right = self._delete_rec(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._minValueNode(node.right)
                node.data = temp.data
                node.right = self._delete_rec(node.right, temp.data)
        return node