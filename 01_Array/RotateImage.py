"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    solution.rotate(matrix)
    print(matrix)



