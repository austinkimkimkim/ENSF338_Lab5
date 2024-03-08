#Chat GPT generated

import random
import timeit
from datetime import datetime


class MergeSort:
    @staticmethod
    def merge(left, right):
        """Merge two sorted arrays."""
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    @staticmethod
    def sort(arr):
        """Sort the array using mergesort."""
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = MergeSort.sort(arr[:mid])
        right = MergeSort.sort(arr[mid:])

        return MergeSort.merge(left, right)


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        self.queue = MergeSort.sort(self.queue)  # Sort the queue using mergesort after each enqueue operation

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)  # Remove and return the first element

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)

class AnotherPriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Insert the new element in the appropriate location to keep the array sorted."""
        if not self.queue:
            self.queue.append(item)
        else:
            index = 0
            while index < len(self.queue) and self.queue[index] <= item:
                index += 1
            self.queue.insert(index, item)

    def dequeue(self):
        """Remove and return the first element of the array."""
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)
    
def generate_random_task_list():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append('enqueue')
        else:
            tasks.append('dequeue')
    return tasks

def measure_performance(queue_type):
    times = []
    for _ in range(100):
        tasks = generate_random_task_list()
        queue = queue_type()
        total_time = timeit.timeit(lambda: execute_tasks(queue, tasks), number=1)
        times.append(total_time)
    return times

def execute_tasks(queue, tasks):
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1) 
        else:
            queue.dequeue()
# Measure performance of PriorityQueue
pq_time = measure_performance(PriorityQueue)
print("Performance of PriorityQueue:", pq_time)

# Measure performance of AnotherPriorityQueue
another_pq_time = measure_performance(AnotherPriorityQueue)
print("Performance of AnotherPriorityQueue:", another_pq_time)

print("Average performance of PriorityQueue:", sum(pq_time)/100)
print("Average performance of AnotherPriorityQueue:", sum(another_pq_time)/100)

#5)
# The AnotherPriorityQueue that we implemented is much faster because its enqueue operation has O(n) complexity, whereas 
# the implementation of PriorityQueue with mergesort has an O(nlogn) enqueue since it must be sorted after each insertion. 
# Since AnotherPriorityQueue doesn't need to call mergesort everytime that we insert a new element into the array, but instead
# just iterates through to the location it needed to be right away and inserts it, this implementation of a priority queue 
# is much faster.