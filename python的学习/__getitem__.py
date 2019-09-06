class Animal(object):

    def __init__(self, animal_list):
        self.animals_name = animal_list

    def __getitem__(self, item):
        return self.animals_name[item]


"在用for ……in 迭代对象时，如果对象没有实现__iter__和__next__迭代器协议" \
"Python的解释器就回去寻找__getitem__方法，如果连__getitem__都没有定义" \
"解释器就会报错" \
"TypeError: 'Animal' object is not iterable" \
"实现__getitem__之后，就可以正常的迭代对象了"
animals = Animal(["dog", "cat", "fish"])
for i in animals:
    print(i)
# dog
# cat
# fish

"当实例对象通过[]运算符取值时，会调用它的__getitem__"

class DataBase(object):

    def __init__(self, id, address):

        self.id = id
        self.address = address
        self.d = {self.id:100,
                  self.address:"219.217.242.90",
                  }

    def __getitem__(self, item):
        return self.d.get(item, "没找到")

data = DataBase(1, "192.168.1.1")

print(data[1])
# 100
print(data["192.168.1.1"])
# 219.217.242.90
print(data[2])
# 没找到
