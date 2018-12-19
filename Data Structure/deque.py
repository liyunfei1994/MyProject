class Deque:

    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def addfront(self, item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0, item)

    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
print(d.items)
d.addfront(10)
print(d.items)
d.addrear("dog")
print(d.items)
d.addfront("cat")
print(d.items)
d.removefront()
print(d.items)
