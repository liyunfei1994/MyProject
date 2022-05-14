class Solution:
    def twoSum(self, nums, target):
    
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i
            print(dct)

A = Solution()
print(A.twoSum(nums=[2,7,11,15], target=22))
