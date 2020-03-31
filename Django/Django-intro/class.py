class Stack (self):
    def __init__(self):
        self.head = None
        
    def pop(self):
        if self.head == None:
            return self
        first = self.head
        self.head = self.head.next
        return first.value


    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self
        
            

class Node (self, value):
    def __init__(self, value):
        self.value = value 
        self.next = None

        
class Queue(self):
    self.head = None
    self.tail = None
    
    def dequeue(self):
        if self.head == None:
            return self
        first = self.head
        self.head = self.head.next
        return first.value
    
    def enqueue(self, value):
        new_node = Node(value)
        self.tail.next = new_node 
        self.tail = new_node
        return self
    
class Node (self, value):
    def __init__(self, value):
        self.value = value 
        self.next = None



def copyStack(self):
    runner = self.head
    newQ = Queue
    while runner != None:
        newQ.enqueue(runner.val)
        runner = runner.next
        copyStack = Stack()
        copyStack.head = newQ.head
        return copyStack