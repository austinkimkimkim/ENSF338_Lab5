import random
import timeit
import matplotlib.pyplot as plt

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
            new_node.setNext(self.head)
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
        else:
            while current.getNext() != self.tail:
                current = current.getNext()
            returnValue = self.tail.getData()
            current.setNext(None)
            self.tail = current
        return returnValue

#Part 4.3
        
def generate_tasks():
    tasks = []
    for _ in range(10000):
        if random.random() < 0.7:
            tasks.append(0) #enqueue
        else:
            tasks.append(1) #dequeue
    return tasks

#Part 4.4

def measure_performance(queue_type):
    times = []
    for _ in range(100):
        tasks = generate_tasks()
        queue = queue_type()
        total_time = timeit.timeit(lambda: execute_tasks(queue, tasks), number=1)
        times.append(total_time)
    return times

def execute_tasks(queue, tasks):
    for task in tasks:
        if task == 0:
            queue.enqueue(1) 
        else:
            queue.dequeue()

array_queue_times = measure_performance(ArrayQueue)
linked_list_queue_times = measure_performance(LinkedListQueue)

#print the arrays of resulting times
print(array_queue_times)
print(linked_list_queue_times)

#Part 4.5
plt.hist(array_queue_times, bins=20, alpha=0.5, label='ArrayQueue')
plt.hist(linked_list_queue_times, bins=20, alpha=0.5, label='LinkedListQueue')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('ArrayQueue vs LinkedListQueue Operation Times')
plt.legend(loc='upper right')
plt.show()

print("Average time for ArrayQueue:", sum(array_queue_times) / len(array_queue_times))
print("Average time for LinkedListQueue:", sum(linked_list_queue_times) / len(linked_list_queue_times))