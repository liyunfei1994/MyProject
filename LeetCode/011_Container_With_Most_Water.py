"""
盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。
"""
class Solution:
    def maxArea(self, height):
        # Two points
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            result = max(min(height[left], height[right]) * (right - left), result)
            if height[left] > height[right]:
                # remove right
                right -= 1
            else:
                # remove left
                left += 1
        return result

A = Solution()
print(A.maxArea([1,8,6,2,5,4,8,3,7]))   # 49
print(A.maxArea([1,8,6]))   # 49
