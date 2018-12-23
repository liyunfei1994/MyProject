class HashTable:

    def __init__(self):
        # hash表的初始大小是11
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        # 计算原始的hash值
        hashvalue = self.hashfunction(key, len(self.slots))
        print("旧的hash值为", hashvalue)
        # print(self.slots == None)
        # 如果原始hash值的地方是None
        if self.slots[hashvalue] == None:
            print("slot[%d] = %s" % (hashvalue, self.slots[hashvalue]))
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            # 如果非空槽，则将旧数据替换为新数据
            if self.slots[hashvalue] == key:
                print("此时新的键和旧的键相同，替换值就可以")
                self.data[hashvalue] = data

            # 如果不是None，也不是key，说明此时发生冲突了
            # 需要更新hash值
            else:
                # 计算新的hash值
                print("此时发生冲突了，同一个槽中放进了不同了键与值，需要重新hash")
                nextslot = self.rehash(hashvalue, len(self.slots))
                print("新的hash值为",nextslot)
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    # 当新的hash值不是None，也不是原有的key时，重新生成
                    print("此时，新的hash值所在的位置，不是None，"
                          "与已有的键不相同，冲突，重新生成hash值")
                    nextslot = self.rehash(nextslot, len(self.slots))
                    print("重新生成hash值为", nextslot)

                if self.slots[nextslot] == None:
                    # 此时没有数据，赋予键与值
                    print("此时，新的hash值所在的位置，键为None")
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    # 此时存在已有的键，赋予新值
                    print("此时，新的hash值所在的位置，已有相同的键，替换值")
                    self.data[nextslot] = data

    def hashfunction(self, key, size):

        return key % size

    def rehash(self, oldhash, size):

        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and \
            not found and not  stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        print("键为%d, 值为\"%s\"" % (key, data))
        self.put(key, data)
        print("键为",self.slots)
        print("值为",self.data)


H = HashTable()
H[54] = "cat"
print()
H[26] = "dag"
print()
H[93] = "lion"
print()
H[17] = "tiger"
print()
H[77] = "bird"
print()
H[31] = "cow"
print()
"""以上这几个，hash值都没有冲突，都很完美"""
"""但是44的hash值为0， 与上面的77冲突了"""
H[44] = "goat"
print()
H[55] = "pig"
print()
H[20] = "chicken"

# print(H.slots)
# print(H.data)
#
# print(H[20])
# print(H[17])
# print(H[99])

键为54, 值为"cat"
旧的hash值为 10
slot[10] = None
键为 [None, None, None, None, None, None, None, None, None, None, 54]
值为 [None, None, None, None, None, None, None, None, None, None, 'cat']

键为26, 值为"dag"
旧的hash值为 4
slot[4] = None
键为 [None, None, None, None, 26, None, None, None, None, None, 54]
值为 [None, None, None, None, 'dag', None, None, None, None, None, 'cat']

键为93, 值为"lion"
旧的hash值为 5
slot[5] = None
键为 [None, None, None, None, 26, 93, None, None, None, None, 54]
值为 [None, None, None, None, 'dag', 'lion', None, None, None, None, 'cat']

键为17, 值为"tiger"
旧的hash值为 6
slot[6] = None
键为 [None, None, None, None, 26, 93, 17, None, None, None, 54]
值为 [None, None, None, None, 'dag', 'lion', 'tiger', None, None, None, 'cat']

键为77, 值为"bird"
旧的hash值为 0
slot[0] = None
键为 [77, None, None, None, 26, 93, 17, None, None, None, 54]
值为 ['bird', None, None, None, 'dag', 'lion', 'tiger', None, None, None, 'cat']

键为31, 值为"cow"
旧的hash值为 9
slot[9] = None
键为 [77, None, None, None, 26, 93, 17, None, None, 31, 54]
值为 ['bird', None, None, None, 'dag', 'lion', 'tiger', None, None, 'cow', 'cat']

键为44, 值为"goat"
旧的hash值为 0
此时发生冲突了，同一个槽中放进了不同了键与值，需要重新hash
新的hash值为 1
此时，新的hash值所在的位置，键为None
键为 [77, 44, None, None, 26, 93, 17, None, None, 31, 54]
值为 ['bird', 'goat', None, None, 'dag', 'lion', 'tiger', None, None, 'cow', 'cat']

键为55, 值为"pig"
旧的hash值为 0
此时发生冲突了，同一个槽中放进了不同了键与值，需要重新hash
新的hash值为 1
此时，新的hash值所在的位置，不是None，与已有的键不相同，冲突，重新生成hash值
重新生成hash值为 2
此时，新的hash值所在的位置，键为None
键为 [77, 44, 55, None, 26, 93, 17, None, None, 31, 54]
值为 ['bird', 'goat', 'pig', None, 'dag', 'lion', 'tiger', None, None, 'cow', 'cat']

键为20, 值为"chicken"
旧的hash值为 9
此时发生冲突了，同一个槽中放进了不同了键与值，需要重新hash
新的hash值为 10
此时，新的hash值所在的位置，不是None，与已有的键不相同，冲突，重新生成hash值
重新生成hash值为 0
此时，新的hash值所在的位置，不是None，与已有的键不相同，冲突，重新生成hash值
重新生成hash值为 1
此时，新的hash值所在的位置，不是None，与已有的键不相同，冲突，重新生成hash值
重新生成hash值为 2
此时，新的hash值所在的位置，不是None，与已有的键不相同，冲突，重新生成hash值
重新生成hash值为 3
此时，新的hash值所在的位置，键为None
键为 [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
值为 ['bird', 'goat', 'pig', 'chicken', 'dag', 'lion', 'tiger', None, None, 'cow', 'cat']

