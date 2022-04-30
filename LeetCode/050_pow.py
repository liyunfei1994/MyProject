"""
/*
解题思路

要判断 n 的正负，以确定我们的底是 x 还是 1/x
经过分析 x^9 = x^4 * x^4 * x = (x^2 * x^2) * (x^2 * x^2) * x
判断 n 的奇偶性，已确定是否需要单独考虑
如果是奇数，那么需要多乘一次 x 本身，因为 Math.floor 向下取整，9 / 2=> 4, 4 + 4 = 8，少了 1 个
如果是偶数，那么不需要考虑，直接降半即可

*/
"""

class Solution:

    def myPow(self, x, n):
        return 1 / self.fast_pow(x, -n) if n < 0 else self.fast_pow(x, n)

    def fast_pow(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        t = self.fast_pow(x, n // 2)

        return t * t * x if n & 1 else t * t

A = Solution()
print(A.myPow(2, 9))

print("5 & 1 = ", 5&1)