"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

"""

class Solution(object):

    def plusOne(self, digits):
        ls = len(digits)
        for index in reversed(range(ls)):
            if digits[index] < 9:
                digits[index] += 1
                # do not need to continue
                return digits
            else:
                # 10
                digits[index] = 0
        # 为了应对99这种情况，需要有下面这一行
        digits.insert(0, 1)
        return digits

A = Solution()
print(A.plusOne([9, 9])) # [1, 0, 0]
print(A.plusOne([9, 9, 9])) # [1, 0, 0, 0]
print(A.plusOne([1, 9, 9])) # [2, 0, 0]
