"""
最大数
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

输入：nums = [10,2]
输出："210"

输入：nums = [3,30,34,5,9]
输出："9534330"
"""

# class LargerNumKey(str):
#     def __lt__(x, y):
#         print("x = ", x)
#         print("y = ", y)
#         print("x + y", x+y)
#         print("y + x", y+x)
#         print("x + y > y + x", x + y > y + x)
#         return x + y > y + x # type x+y <class 'str'>
#
#
# class Solution:
#     def largestNumber(self, nums):
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num
#
#
# nums = [10, 20, 8]
# print(nums)
# # print(list(map(str, nums)))
# #
# # print(sorted(map(str, nums), key=LargerNumKey))
# # # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# # print('--'.join(['10', 'A', 'B']))  # 10--A--B
#
# A = Solution()
# print(A.largestNumber(nums))

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 思想：使用冒泡法，对于[a,b]中若a+b < b+a，则将a,b的顺序进行交换
        # 冒泡法，总共有n-1趟，第一趟走完，把最小的放在最后面
        for i in range(len(nums) - 1):
            for j in range(0, len(nums) - 1 - i):
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

        res = ""
        for i in range(len(nums)):
            res = res + str(nums[i])

        return str(int(res))

A = Solution()
print(A.largestNumber([10, 8, 9, 12]))
