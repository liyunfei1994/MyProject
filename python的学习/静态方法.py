class Dog(object):

    @staticmethod
    def run():

        "不访问实例属性和类属性"
        "就可以将其设置为静态方法"
        
        print("小狗要跑。。。")


"通过 类名. 调用静态方法"
"不需要创建对象"

Dog.run()
