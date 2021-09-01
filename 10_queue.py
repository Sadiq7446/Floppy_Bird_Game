""" Python Script to create a queue and perform various operations on it """

# Write your code from here

from queue import Queue

queue_01 = Queue()

print("Number of elements in the queue: ", queue_01.qsize())

# Adding of element to queue

queue_01.put('a')
queue_01.put('b')
queue_01.put('c')
queue_01.put('d')
print("\nNumber of elements in the queue: ", queue_01.qsize())

# Removing element from queue
print("\nElements dequeued from the queue")
print(queue_01.get())
print(queue_01.get())
print(queue_01.get())
print(queue_01.get())

