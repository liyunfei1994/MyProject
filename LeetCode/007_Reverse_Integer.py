"""
整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
输入：x = 123
输出：321
输入：x = -123
输出：-321
输入：x = 120
输出：21
"""

class Solution(object):

    def reverse(self, x):
        # Note that in Python -1 / 10 = -1
        res, isPos = 0, 1
        if x < 0:
            isPos = -1
            x = -1 * x
        while x != 0:
            res = res * 10 + x % 10
            if res > 2147483647:
                # print("大于")
                return 0
            x //= 10
        return res * isPos

A = Solution()
print(A.reverse(123)) # 321
print(A.reverse(120)) # 21
