"""
最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

动态规划
状态定义：dp[i] 表示以 num[i] 结尾的连续子数组的最大和

这种情况下，nums[i] 必须被选取

状态转移方程：
        如果 dp[i-1] > 0, dp[i] = dp[i-1] + num[i]
        如果 dp[i-1] <= 0, dp[i] = nums[i]

初始化：dp[0] = nums[0]

复杂度分析：
时间复杂度：O(N)  只遍历了一次数组
空间复杂度：O(N)  状态数组的长度为N

固定住了不确定的因素，使得状态转移变得容易
求解过程中每个子问题只求解一次

"""

class Solution(object):

    def maxSubArray(self, nums):
        maxEndingHere = maxSofFar = nums[0]
        for i in range(1, len(nums)):
            # dp[i] = max(dp[i-1] + nums[i], nums[i])
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSofFar = max(maxEndingHere, maxSofFar)
        return maxSofFar

A = Solution()
print(A.maxSubArray([1,2,3]))   # 6
print(A.maxSubArray([-1, -2, 3, 4]))    # 7
print(A.maxSubArray([5,4,-1,7,8]))  # 23
print(A.maxSubArray([-5,4,-1,7,8]))  # 18
