

class Solution(object):
    # def threeSum(self, nums):
    #     # skip duplicate
    #     # O(n^3)
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()
    #     ls = len(nums)
    #     result = []
    #     for i in range(0, ls - 2):
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         j = i + 1
    #         k = ls - 1
    #         while(j < k):
    #             temp = [nums[i], nums[j], nums[k]]
    #             s = sum(temp)
    #             jtemp = nums[j]
    #             ktemp = nums[k]
    #             if s <= 0:
    #                 j += 1
    #                 while(j < k and jtemp == nums[j]):
    #                     j += 1
    #                 if s == 0:
    #                     result.append(temp)
    #             else:
    #                 k -= 1
    #                 while(j < k and ktemp == nums[k]):
    #                     k -= 1
    #     return result
    # def threeSum(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #     """
    #     # using multiple 2 sum
    #     nums.sort()
    #     result, visited = set(), {}
    #     for i in xrange(len(nums) - 2):
    #         table, target = {}, -nums[i]
    #         if nums[i] not in visited:
    #             for j in xrange(i + 1, len(nums)):
    #                 if nums[j] not in table:
    #                     table[target - nums[j]] = j
    #                 else:
    #                     result.add((nums[i], target - nums[j], nums[j]))
    #             visited[nums[i]] = 1
    #     return list(result)

    def threeSum(self, nums):
        res = []
        nums.sort()
        print("num = ", nums)
        ls = len(nums)
        for i in range(ls - 2):
            print("i = ", i)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                print("curr = ", curr)
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    print("res = ", res)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return res

A = Solution()
# print(A.threeSum([-1, 0, 1, 2, -1, -4]))
print(A.threeSum([-3, 2, 4, 2, -1, -1, -5]))

"""
num =  [-5, -3, -1, -1, 2, 2, 4]
i =  0
curr =  -4
curr =  -2
curr =  -2
curr =  1
curr =  -1
i =  1
curr =  0
res =  [[-3, -1, 4]]
curr =  1
i =  2
curr =  2
curr =  0
res =  [[-3, -1, 4], [-1, -1, 2]]
i =  3
i =  4
curr =  8
[[-3, -1, 4], [-1, -1, 2]]

"""