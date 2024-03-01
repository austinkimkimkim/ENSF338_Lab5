class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): #enqueue at the head
        self.queue.insert(0,item)

    def dequeue(self): #dequeue at the tail
        temp = self.queue[-1]
        self.queue.pop()
        return temp

