import stack
import binarytree


def buildparsetree(fpexp):
    fplist = fpexp.split()
    # ['(', '(', '10', '+', '5', ')', '*', '3', ')']
    print(fplist)
    pstack = stack.Stack()
    # []
    print(pstack.items)
    # 构建一个根节点为空的空树
    etree = binarytree.BinaryTree('')
    print("根节点空树etree的地址为%X" % id(etree))
    print("根节点的值etree.key:",etree.key)
    # 将一个二叉树对象存入了列表栈中
    print("将根节点的空树放入栈中")
    pstack.push(etree)
    print("栈中空树的地址为%X" % id(pstack.items[0]))
    # 当前节点为根节点
    currenttree = etree
    print("current tree的地址为:%X" % id(currenttree))

    print("current getrightchild:", currenttree.getrightchild())
    print()
    for i in fplist:
        print("i=", i)
        if i == '(':
            print("此时i=", i)
            print("i = '(',getleftchild:", currenttree.getleftchild())
            currenttree.insertleft('')
            print("insert 之后左节点的值为:", currenttree.getleftchild().getrootval())
            print("当前树的地址为%X" % id(currenttree))
            pstack.push(currenttree)
            print("栈插入currenttree之后地址分别为",
                  [hex(id(pstack.items[i])) for i in range(len(pstack.items))])
            print("将当前树的节点移至左节点")
            currenttree = currenttree.getleftchild()
            print("此时currenttree地址为:%X" % id(currenttree))
            print()

        elif i not in ['+', '-', '*', '/', ')']:
            print("此时i=", i, "不在那些运算符里，是数字")
            print("此时currenttree的地址为%X" % id(currenttree))
            print("设置此时currenttree的节点值")
            currenttree.setrootval(int(i))
            print("此时currenttree的节点值为",currenttree.getrootval())
            print("从栈中弹出父节点")
            parent = pstack.pop()
            print("父节点的地址为%X" % id(parent))
            print("将当前节点转移至父节点")
            currenttree = parent
            print("父节点的地址为%X" % id(currenttree))
            print()

        elif i in ['+', '-', '*', '/']:
            print("此时i为运算符", i)
            print("当前树的地址为%X" % id(currenttree))
            print("给当前的节点赋予值", i)
            currenttree.setrootval(i)
            print("当前节点的值为", i)
            print("给当前的节点插入右子树")
            currenttree.insertright('')
            print("将当前的树放入栈中")
            pstack.push(currenttree)
            print("此时栈中树的地址为", [hex(id(i)) for i in range(len(pstack.items))])
            print("将当前节点取为右节点")
            currenttree = currenttree.getrightchild()
            print("当前节点的地址为%X" % id(currenttree))
            print()

        elif i ==')':
            print("此时i=",i)
            print("从栈中弹出获得父节点")
            currenttree = pstack.pop()
            print("父节点的地址为%X" % id(currenttree))
            print()

        else:
            raise ValueError

    return etree


pt=buildparsetree("( ( 10 + 5 ) * 3 )")


['(', '(', '10', '+', '5', ')', '*', '3', ')']
[]
根节点空树etree的地址为1A390208EF0
根节点的值etree.key: 
将根节点的空树放入栈中
栈中空树的地址为1A390208EF0
current tree的地址为:1A390208EF0
current getrightchild: None

i= (
此时i= (
i = '(',getleftchild: None
新的二叉树对象地址为1A390204390：
insert 之后左节点的值为: 
当前树的地址为1A390208EF0
栈插入currenttree之后地址分别为 ['0x1a390208ef0', '0x1a390208ef0']
将当前树的节点移至左节点
此时currenttree地址为:1A390204390

i= (
此时i= (
i = '(',getleftchild: None
新的二叉树对象地址为1A390204358：
insert 之后左节点的值为: 
当前树的地址为1A390204390
栈插入currenttree之后地址分别为 ['0x1a390208ef0', '0x1a390208ef0', '0x1a390204390']
将当前树的节点移至左节点
此时currenttree地址为:1A390204358

i= 10
此时i= 10 不在那些运算符里，是数字
此时currenttree的地址为1A390204358
设置此时currenttree的节点值
此时currenttree的节点值为 10
从栈中弹出父节点
父节点的地址为1A390204390
将当前节点转移至父节点
父节点的地址为1A390204390

i= +
此时i为运算符 +
当前树的地址为1A390204390
给当前的节点赋予值 +
当前节点的值为 +
给当前的节点插入右子树
新的二叉树对象地址为1A3902043C8：
将当前的树放入栈中
此时栈中树的地址为 ['0x5b186c00', '0x5b186c20', '0x5b186c40']
将当前节点取为右节点
当前节点的地址为1A3902043C8

i= 5
此时i= 5 不在那些运算符里，是数字
此时currenttree的地址为1A3902043C8
设置此时currenttree的节点值
此时currenttree的节点值为 5
从栈中弹出父节点
父节点的地址为1A390204390
将当前节点转移至父节点
父节点的地址为1A390204390

i= )
此时i= )
从栈中弹出获得父节点
父节点的地址为1A390208EF0

i= *
此时i为运算符 *
当前树的地址为1A390208EF0
给当前的节点赋予值 *
当前节点的值为 *
给当前的节点插入右子树
新的二叉树对象地址为1A390204400：
将当前的树放入栈中
此时栈中树的地址为 ['0x5b186c00', '0x5b186c20']
将当前节点取为右节点
当前节点的地址为1A390204400

i= 3
此时i= 3 不在那些运算符里，是数字
此时currenttree的地址为1A390204400
设置此时currenttree的节点值
此时currenttree的节点值为 3
从栈中弹出父节点
父节点的地址为1A390208EF0
将当前节点转移至父节点
父节点的地址为1A390208EF0

i= )
此时i= )
从栈中弹出获得父节点
父节点的地址为1A390208EF0
