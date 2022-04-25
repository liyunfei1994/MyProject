class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        pos = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1
            pos -= 1
        print("nums1 ", nums1)
        # 用于处理特殊情况
        while p2 >= 0:
            nums1[pos] = nums2[p2]
            p2 -= 1
            pos -= 1
        print("nums1 ", nums1)


A = Solution()
A.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
A.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
"""
nums1  [1, 2, 2, 3, 5, 6]
nums1  [1, 2, 2, 3, 5, 6]
nums1  [0]
nums1  [1]
"""