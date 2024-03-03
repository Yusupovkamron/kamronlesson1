class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: stack is empty")


    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: stack is empty")

    def size(self):
        return len(self.items)
stack = stack()

print(stack.is_empty)
print(stack.size)

stack.push(2)
stack.push(5)
stack.push(7)
stack.push(9)
print('Queue')
for i in stack.items:
    print(f"{i}")

    


print("Stack")
for j in stack.items[-1::-1]:
    print(f"{j}")




















