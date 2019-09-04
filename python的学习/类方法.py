class Tool(object):

    "类属性， 在类名下方使用 赋值语句 进行定义"
    "用来记录 与这个类相关 的特征"

    count = 0

    @classmethod
    def show_tool_count(cls):

        "在类方法的内部, 要想访问当前这个类的属性， 使用 cls. 访问"
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):

        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("锤子")

"访问类方法，使用 类名. "
Tool.show_tool_count()
