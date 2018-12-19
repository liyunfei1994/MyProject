class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext


temp = Node(10)
print(temp.data)
print(temp.next)
print(temp.getdata())
