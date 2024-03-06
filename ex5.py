#1
class ArrQueue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.queue = [None] * capacity
    self.head = -1
    self.tail = -1

  def is_empty(self):
    return self.head == -1
  def is_full(self):
    return (self.tail + 1)% self.capacity == self.head
  
  def enqueue(self, item):
    if(self.is_full()):
      print('Enqueue None')
      return
    elif self.is_empty():
      self.head = 0
      self.tail = 0
    else:
      self.tail = (self.tail +1) % self.capacity
    self.queue[self.tail] = item
    print('Enqueue', item)

  def dequeue(self):
    if(self.is_empty()):
      print('Dequeue None')
      return None
    item = self.queue[self.head]
    if self.head == self.tail:
      self.head = -1
      self.tail = -1
    else:
      self.head = (self.head +1) % self.capacity    
    print('Dequeue', item)
    return item

  def peek(self):
    if(self.is_empty()):
      print('Peak None')
      return   
    print('Peek', self.queue[self.head])
    return self.queue[self.head]
         

#2
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedQueue:
  def __init__(self, capacity):
    self.head = None
    self.tail = None
    self.size = 0
    self.capacity = capacity

  def enqueue(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
      self.head.next = self.head
      print('Enqueue', data)
      self.size = 1
      return
    elif self.size == self.capacity:
      print('Enqueue None')
      return
    else:
      newNode.next = self.head
      self.tail.next = newNode
      self.tail = newNode
      print('Enqueue', data)
      self.size += 1

  def dequeue(self):
    if self.head is None:
      print('Dequeue None')
      return
    temp = self.head.data
    if self.head == self.tail:
      self.head = None
      self.tail = None
      print('Dequeue', temp)
      self.size = 0
    else:
      self.head = self.head.next
      self.tail.next = self.head
      print('Dequeue', temp)
      self.size -=1
    return temp
  
  def peek(self):
    if self.head is None:
      print('Peek None')
      return
    else:
      print('Peek', self.head.data)
      return self.head.data
                    
      
#3
arr = ArrQueue(18)
ll = LinkedQueue(18)

def generateTests(queue):
  #dequeue from empty queue
  queue.dequeue()
  print("Expected is: Dequeue None")
  #peek into empty queue
  queue.peek()
  print("Expected is: Peak None")
  #Enqueue into list 18 times
  for i in range(18):
    queue.enqueue(i)
    print('Expected is: ', f'Enqueue {i}')
  #Enqueue into full queue
  queue.enqueue(18)
  print('Expected is: Enqueue None')
  #Dequeue from list 18 times
  for j in range(18):
    queue.dequeue()
    print('Expected is: ', f'Dequeue {j}')
  #Enqueue for last time
  queue.enqueue(1)
  print('Expected is: Enqueue 1')

generateTests(arr)
generateTests(ll)