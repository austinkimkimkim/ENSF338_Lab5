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

stack = StackArr()
stack.push(2)
stack.push(3)
stack.print()

list = linkedList()
list.push(3)
list.push(2)
list.print()

def generateList(length):
  l = []
  for i in length:
    
