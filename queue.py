class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


a = Queue()

print(a.isEmpty())
a.enqueue("Exercise 1")
a.enqueue("Exercise 2")
a.enqueue("Exercise 3")
a.enqueue("Exercise 4")
print(a.dequeue())
a.enqueue("Exercise 5")
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.isEmpty())
print(a.dequeue())
print(a.isEmpty())