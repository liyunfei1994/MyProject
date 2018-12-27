class BinaryTree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None
        # print(self)

    def insertleft(self, newnode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self, newnode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getrightchild(self):
        return self.rightchild

    def getleftchild(self):
        return self.leftchild

    def setrootval(self, obj):
        self.key = obj

    def getrootval(self):
        return self.key


r = BinaryTree('jordan')
# r.setrootval('kobe')
print("获得根节点的值",r.getrootval())
# print(r.getleftchild())
r.insertleft('kobe')
print("获得左边路径引用的子节点",r.getleftchild(),"是一个二叉树对象")
print("获得左边子节点的值",r.getleftchild().getrootval())
r.insertright('lebron')
print("获得右边路径引用的子节点",r.getrightchild(),"是一个二叉树对象")
print("获得右边子节点的值",r.getrightchild().getrootval())

r.insertright('iversion')
# 原来的右节点向下移了一层
print("获得插入新节点之后的右叶子结点的值",r.getrightchild().getrightchild().getrootval())


获得根节点的值 jordan
获得左边路径引用的子节点 <__main__.BinaryTree object at 0x000001FB3D968D30> 是一个二叉树对象
获得左边子节点的值 kobe
获得右边路径引用的子节点 <__main__.BinaryTree object at 0x000001FB3D968DA0> 是一个二叉树对象
获得右边子节点的值 lebron
获得插入新节点之后的右叶子结点的值 lebron
