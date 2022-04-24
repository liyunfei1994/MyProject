"""
杨辉三角
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            result.append([0] * (i + 1))
        print("result ", result)
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

A =Solution()
print(A.generate(numRows=5))
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# print(A.generate(numRows=2))
# [[1], [1, 1]]