#Chat GPT generated

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
            print("Priority queue is empty")
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
            print("Priority queue is empty")
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)

# Example usage:
pq = PriorityQueue()
pq.enqueue(3)
pq.enqueue(1)
pq.enqueue(4)
pq.enqueue(2)

print("Priority Queue:", pq)  # Output: [1, 2, 3, 4]

print("Dequeue:", pq.dequeue())  # Output: 1
print("Priority Queue:", pq)  # Output: [2, 3, 4]


pq = AnotherPriorityQueue()
pq.enqueue(3)
pq.enqueue(1)
pq.enqueue(4)
pq.enqueue(2)

print("Another Priority Queue:", pq)  # Output: [1, 2, 3, 4]

print("Another Dequeue:", pq.dequeue())  # Output: 1
print("Another Priority Queue:", pq)  # Output: [2, 3, 4]