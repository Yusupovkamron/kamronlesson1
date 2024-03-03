class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue("ali")
queue.enqueue(3)
# print(queue.size())
# print(queue.is_empty())
queue.enqueue("a")
print(queue.items)

print("This is Stack")
for i in queue.items[-1::-1]:
    print(i)

print("This is Queue")
for i in queue.items:
    print(i)


