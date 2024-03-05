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
plt.hist(array_queue_times, bins=20, alpha=0.5, label='ArrayQueue',color='red')
plt.hist(linked_list_queue_times, bins=20, alpha=0.5, label='LinkedListQueue', color='blue')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('ArrayQueue vs LinkedListQueue Operation Times')
plt.legend(loc='upper right')
plt.show()

#The values for the array queue are barely visible on the histogram, so let's create a scatterplot as well
plt.scatter(range(len(array_queue_times)), array_queue_times, label='ArrayQueue', color='red')
plt.scatter(range(len(linked_list_queue_times)), linked_list_queue_times, label='LinkedListQueue', color='blue')
plt.xlabel('Iteration')
plt.ylabel('Time (seconds)')
plt.title('ArrayQueue and LinkedListQueue Operation Times')
plt.legend()
plt.show()

print("Average time for ArrayQueue:", sum(array_queue_times) / len(array_queue_times))
print("Average time for LinkedListQueue:", sum(linked_list_queue_times) / len(linked_list_queue_times))

#From the plots, we can see that the array implementation is much faster than the linked list implementation.
# Since the linked list implementation has an O(1) enqueue complexity and O(n) dequeue complexity, but the 
# array implementation has O(n) enqueue and O(1) dequeue, we would expect the linked list implementation
# to be much faster since 70% of the operations are to enqueue. The likely reason for this is how complexity 
# is not an empirical measure of the time it will take for the queue to complete. For example, even though
# creating a new node and changing the head pointer in a linked list is O(1), it may be a more costly and 
# time consuming operation than compared to adding the element to the beginning of an array and shifting 
# every element over, even though this should be O(n). 