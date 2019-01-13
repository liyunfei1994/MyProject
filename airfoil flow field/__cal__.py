class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print("my name is %s" % self.name)
        print("my friend is %s" % friend)


p = Person("李云飞", "大黄狗")
p("小明")

my name is 李云飞
my friend is 小明

在python中函数其实是一个对象
所有的函数都是可调用对象
一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
单看 p("小明") 你无法确定 p 是一个函数还是一个类实例，所以，在Python中，函数也是对象，对象和函数的区别并不显著。
