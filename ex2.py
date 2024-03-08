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
    
def generate_random_task_list(length):
    tasks = []
    for _ in range(length):
        # Generate a random task based on probabilities
        task = random.choices(['enqueue', 'dequeue'], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

def generate_random_task_list():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:
            tasks.append('enqueue')
        else:
            tasks.append('dequeue')
    return tasks

def measure_performance(pq_class):
    total_time = 0
    for _ in range(100):
        tasks = generate_random_task_list()
        pq = pq_class()
        start_time = datetime.now()
        for task in tasks:
            if task == 'enqueue':
                pq.enqueue(random.randint(1, 1000))
            else:
                pq.dequeue()
        end_time = datetime.now()
        total_time += (end_time - start_time).total_seconds()
    return total_time

# Measure performance of PriorityQueue
pq_time = measure_performance(PriorityQueue)
print("Performance of PriorityQueue:", pq_time)

# Measure performance of AnotherPriorityQueue
another_pq_time = measure_performance(AnotherPriorityQueue)
print("Performance of AnotherPriorityQueue:", another_pq_time)


# The AnotherPriorityQueue that we implemented is much faster because when we don't do the mergesort everytime that we insert something into our array, we instead just found the location it needed to be right away and inserted it
# while in our original PriorityQueue we mergesorted every single time we added a new element which takes more time