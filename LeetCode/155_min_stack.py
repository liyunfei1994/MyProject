"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素

"""

import math

# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = [math.inf]
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         self.min_stack.append(min(x, self.min_stack[-1]))
#
#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min_stack[-1]

# 面试的时候被问到不能用额外空间，就去网上搜了下不用额外空间的做法。思路是栈里保存差值。

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # 栈里保存差值
        self.min_value = -1

    def push(self, x: int) -> None:
        if not self.stack:  # 如果栈为空
            self.stack.append(0)    # 栈中压入0
            self.min_value = x  # 最小值为当前的值
        else:               # 栈不为空
            diff = x-self.min_value
            self.stack.append(diff)
            self.min_value = self.min_value if diff > 0 else x

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_value
                self.min_value = top - diff
            else:
                top = self.min_value + diff
            return top

    def top(self) -> int:
        return self.min_value if self.stack[-1] < 0 else self.stack[-1] + self.min_value

    def getMin(self) -> int:
        return self.min_value if self.stack else -1

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
