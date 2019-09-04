class Tool(object):

    "类属性， 在类名下方使用 赋值语句 进行定义"
    "用来记录 与这个类相关 的特征"

    count = 0

    def __init__(self, name):

        self.name = name

        Tool.count += 1


tool1 = Tool("锤子")
tool2 = Tool("斧子")
tool3 = Tool("水桶")

print(Tool.count)
