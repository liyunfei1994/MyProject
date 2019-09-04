class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩" % self.name)


class Xtq(Dog):

    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s 和 %s 快乐的玩。。。" % (self.name, dog.name))

        dog.game()


# wangcai = Dog("旺财")
wangcai = Xtq("哮天犬")

xiaoming = Person("小明")

xiaoming.game_with_dog(wangcai)

# 在Person类中 只需要让狗对象调用game方法，而不用关心是什么狗
# game 方法 是在Dog父类中定义的
# 程序执行时， 传入不同的狗对象，产生不同的执行效果
# 多态  以继承和重写父类方法为前提  增加代码的灵活度
