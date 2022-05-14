"""
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""

class Solution:
    def findRepeatNumber(self, nums):
        temp_set = set()
        repeat = -1
        for i in range(len(nums)):
            temp_set.add(nums[i])
            if len(temp_set) < i + 1:
                repeat = nums[i]
                break
        return repeat


A = Solution()
print(A.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))
