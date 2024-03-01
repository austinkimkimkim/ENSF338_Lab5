#Part 4.1

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): #enqueue at the head
        self.queue.insert(0,item)

    def dequeue(self): #dequeue at the tail
        if len(self.queue) != 0:
            temp = self.queue[-1]
            self.queue.pop()
            return temp
        else:
            return "queue is empty! "
    
#Part 4.2
        
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.setNext(self.head)
            self.head = new_node

    def dequeue(self):
        current = self.head
        if current == None:
            return None
        if current.getNext() == None:
            returnValue = current.getData()
            self.head = None
            self.tail = None
            return returnValue
        else:
            while current.getNext() != self.tail:
                current = current.getNext()
            returnValue = self.tail.getData()
            current.setNext(None)
            self.tail = current
            return returnValue


