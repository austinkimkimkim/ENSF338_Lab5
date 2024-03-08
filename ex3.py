import random
import timeit
from matplotlib import pyplot as plt

def main():
  #1. 
  class StackArr:
    def __init__(self):
      self.stack = []
    def push(self, val):
      self.stack.append(val)  
    def pop(self):
      if len(self.stack) == 0:
        return
      else:
        self.stack.pop()
    def print(self):
      print(self.stack)
    
  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

  class linkedList:
    def __init__(self):
      self.head = None
    def push(self, element):
      new_node = Node(element)
      if self.head == None:
        self.head = new_node
        new_node.next = None
        return
      else:
        new_node.next = self.head
        self.head = new_node
    def pop(self):
      if self.head == None:
        return
      else:
        node = self.head
        self.head = node.next
        node = None
    def print(self):
      current = self.head
      while(current != None):
        print(current.data)
        current = current.next

  # stack = StackArr()
  # stack.push(2)
  # stack.push(3)
  # stack.print()

  # list = linkedList()
  # list.push(3)
  # list.push(2)
  # list.print()

  def generateList():
    tasks = []
    for _ in range(10000):
      if random.random() < 0.7:
        tasks.append("push")
      else:
        tasks.append("pop")
    return tasks

  def doTask(stack, tasks):
    for task in tasks:
      if task == 'push':
        stack.push(1)
      elif task == 'pop':
        stack.pop()
    

  arrTime = []
  linkedTime = []

  for _ in range(100):
    tasks = generateList()
    arr = StackArr()
    list = linkedList()
    arrTime.append(timeit.timeit(lambda: doTask(arr, tasks), number= 1))
    linkedTime.append(timeit.timeit(lambda: doTask(list, tasks), number =1))
  
  print("Time for array stack: ", arrTime)
  print("Time for linked list stack: ", linkedTime)

  plt.hist(arrTime, alpha = 0.5)
  plt.hist(linkedTime, alpha = 0.5)
  plt.xlabel('Time(seconds)')
  plt.ylabel('Frequency')
  plt.legend(['Array', "Linked List"])
  plt.show()



if __name__ == '__main__':
  main()

#5. The linked list implementaion of the stack was slower than the array implementation of the stack
# because popping and pushing using linked list takes a little bit more work than arrays. 