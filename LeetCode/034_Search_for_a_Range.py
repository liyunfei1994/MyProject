"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

输入：nums = [], target = 0
输出：[-1,-1]

"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]
        min = 0
        max = length - 1
        while min <= max:
            pos = (min + max) // 2
            if nums[pos] > target:
                max = pos - 1
            elif nums[pos] < target:
                min = pos + 1
            else:
                # when nums[pos] == target
                # find the min and max
                for i in range(min, max + 1):
                    if nums[i] == target:
                        if min < i and nums[min] != nums[i]:
                            min = i
                        max = i
                return [min, max]
        return [-1, -1]

A = Solution()
print(A.searchRange([5, 7, 7, 8, 9, 10], target=8))