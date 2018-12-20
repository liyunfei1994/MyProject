import node


class UnorderedList:

    def __init__(self):
        """链表类本身不包含任何节点对象"""
        """相反，只包含对链接结构中第一个节点的单个引用"""
        self.head = None

    def isempty(self):
        """检查链表头是否是None引用"""
        """只有在链表中没有节点时才为真"""
        return self.head == None

    def add(self, item):
        """创建一个新节点并将该项作为其数据"""
        """链表的每一项驻留在节点对象中"""
        print("链表头的旧引用", hex(id(self.head)))
        temp = node.Node(item)
        print("节点",temp.data)
        print("节点的地址",hex(id(temp)))
        """更改新节点的下一个引用，以引用旧链表的第一个节点"""
        temp.setnext(self.head)
        print("节点的新的引用",hex(id(temp.next)))
        """修改链表的头以引用新节点"""
        self.head = temp
        print("链表的头新引用",hex(id(self.head)))

    def size(self):
        """current是外部引用，初始化为链表的头部"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getnext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()

        return found


mylist = UnorderedList()
mylist.add(31)
print()
mylist.add(77)
print()
mylist.add(17)

链表头的旧引用 0x718aa490
节点 31
节点的地址 0x161fbf47d30
节点的新的引用 0x718aa490
链表的头新引用 0x161fbf47d30

链表头的旧引用 0x161fbf47d30
节点 77
节点的地址 0x161fbf47dd8
节点的新的引用 0x161fbf47d30
链表的头新引用 0x161fbf47dd8

链表头的旧引用 0x161fbf47dd8
节点 17
节点的地址 0x161fbf47e10
节点的新的引用 0x161fbf47dd8
链表的头新引用 0x161fbf47e10
