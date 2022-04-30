import numpy as np

"""
void rotate(int** matrix, int matrixSize, int* matrixColSize){
    //先转置矩阵
    for (int i = 0; i < matrixSize; ++i)
        for (int j = 0; j < i; ++j){
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    
    //再镜像对称
    int left = 0;
    int right = matrixSize - 1;
    while (left < right){
        for (int i = 0; i < matrixSize; ++i){
            int temp = matrix[i][left];
            matrix[i][left] = matrix[i][right];
            matrix[i][right] = temp;
        }
        left++;
        right--;
    }   
}
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # rotate from outside to inside
        print(np.array(matrix))
        for i in range(len(matrix)):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        left = 0
        right = len(matrix) - 1
        while left < right:
            for i in range(len(matrix)):
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp

            left += 1
            right -= 1
        print(np.array(matrix))

s = Solution()
s.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
[[13  9  5  1]
 [14 10  6  2]
 [15 11  7  3]
 [16 12  8  4]]
"""