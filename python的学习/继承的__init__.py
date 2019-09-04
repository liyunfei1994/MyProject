class Parent(object):

    def __init__(self, name):

        self.name = name
        print("create an instance of:", self.__class__.__name__)
        print("name attribute is:", self.name)


class Child(Parent):
    pass

"子类实例化时， 由于子类没有初始化，此时 父类的初始化函数就会被默认调用"
c = Child("init Child")

print(" == " * 10)
class Parent(object):

    def __init__(self, name):
        self.name = name
        print("create an instance of:", self.__class__.__name__)
        print("name attribute is:", self.name)


class Child(Parent):

    def __init__(self):
        print("call __init__ from Child class")


c = Child()

"在子类中没有显式调用父类的初始化函数， 则父类的属性不会被初始化，因此子类中 name属性不存在"
print(c.name)
# AttributeError: ‘Child’ object has no attribute ‘name’

# ========================================================

class Parent(object):

    def __init__(self, name):
        self.name = name
        print("create an instance of:", self.__class__.__name__)
        print("name attribute is:", self.name)


class Child(Parent):

    def __init__(self):
        print("call __init__ from Child class")
        super(Child, self).__init__("data from Child")

d = Parent("Tom")

"子类定义了自己的初始化函数，显式调用了父类的初始化方法，子类和父类的属性都会被初始化"

c = Child()
print(c.name)

"super 的使用详解"
"super 主要用来调用父类方法 来 显示调用父类"
class Parent(object):
    value = "Hi, Parent value"
    def fun(self):
        print("This is from Parent")

class Child(Parent):
    value = "Hi, Child value"
    def ffun(self):
        print("This is from Child")

c = Child()
c.fun()
c.ffun()
print(Child.value)

"有时候需要在子类中访问父类的一些属性" \
"可以通过父类名直接访问父类的属性" \
"当调用父类的方法时， 需要将self显式的传递进去"

class Parent(object):
    value = "Hi, Parent value"
    def fun(self):
        print("This is from Parent")


class Child(Parent):
    value = "Hi, Child value"
    def fun(self):
        print("This is from Child")
        Parent.fun(self)

c = Child()
c.fun()

class Parent(object):
    value = "Hi, Parent value"
    def fun(self):
        print("This is from Parent")


class Child(Parent):
    value = "Hi, Child value"
    def fun(self):
        print("This is from Child")
        # Parent.fun(self)
        "调用父类的fun函数方法"
        super(Child, self).fun()

c = Child()
c.fun()
