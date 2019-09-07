class Student(object):

    def __init__(self, *args):
        self.name = args
        print("*args", *args)
        print("args",args)
        print("self.name", self.name)
        print("self.name is args", self.name is args)

    def __len__(self):
        return len(self.name)

"有两种情况需要注意" \
"第一种是将列表直接传进去"

students = ["Bob", "Lisa", "Tom", "Lili"]
s = Student(students)
# *args ['Bob', 'Lisa', 'Tom', 'Lili']
# args (['Bob', 'Lisa', 'Tom', 'Lili'],)
# self.name (['Bob', 'Lisa', 'Tom', 'Lili'],)
# self.name is args True
# 1
"此时，将列表作为*args传进来，args接受tuple" \
"使得args元组中只有一个列表元素"
print(len(s))  # 长度为1

# ===========================================
"将*列表传进去" \
"args就是将列表的中括号脱去"
students = ["Bob", "Lisa", "Tom", "Lili"]
s = Student(*students)
print(len(s))

# 由此可见，传入可变参数，一定要传进去*args
#*args Bob Lisa Tom Lili
#args ('Bob', 'Lisa', 'Tom', 'Lili')
#self.name ('Bob', 'Lisa', 'Tom', 'Lili')
#self.name is args True
#4
