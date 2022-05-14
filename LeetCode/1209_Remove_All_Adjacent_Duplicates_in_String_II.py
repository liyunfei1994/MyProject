"""
1209, 删除字符串中的所有的相邻重复项

我们准备一个栈stack，栈中的每个元素是个包含两个元素的数组，
第一个元素是字符，第二个元素是该字符到当前位置为止已经连续出现过的次数。
这个栈的维护也是很简单的，分成两种情况，
如果新加入的字符和栈顶元素不同，说明遇到新字符，需要将该字符及其出现次数1入栈，
否则，需要将栈顶元素的出现次数+1。

这里需要注意的是，每当栈被更新，都需要判断一下栈顶字符的出现次数stack[-1][1]是否已经达到k，
如果达到，则将栈顶元素弹出，意为删除连续出现k次的字符。
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:           # 栈为空或者遇到新字符
                stack.append([c, 1])                     # 将该字符及其出现次数1入栈
            else:
                stack[-1][1] += 1                           # 计数器加1
            if k == stack[-1][1]:                           # 计数器满足条件
                stack.pop()                                 # 删除重复字符
            print(stack)
        return ''.join(c * n for c, n in stack)


s = Solution()
print(s.removeDuplicates("deeedbbcccbdaa", 3))
# aa
# print(s.removeDuplicates("pbbcggttciiippooaais", 2))
# ps
