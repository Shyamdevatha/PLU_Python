class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinedList:
    def __init__(self):
        self.head=None
        
    def insert_start(self, data):
        new_node= Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    
    def insert_betw(self, data, prev):
        new_node =Node(data)
        new_node.ref = prev.ref
        prev.ref = new_node
        
        
    def del_start(self):
        del_node= self.head
        self.head = self.head.ref
        del_node.ref = None
        
    def del_bet(sefl, prev):
        prev.ref = prev.ref.ref
        prev.ref.ref = None