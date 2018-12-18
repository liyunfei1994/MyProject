class Queue():
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.isempty())
q.enqueue(9)
print(q.items)
q.enqueue(10)
print(q.items)
q.enqueue("dog")
print(q.items)
q.dequeue()
print(q.items)
