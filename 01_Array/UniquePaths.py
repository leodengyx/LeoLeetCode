"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = []
        for i in range(n):
            matrix.append([None] * m)
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    matrix[i][j] = 1
                elif i == 0 and j != 0:
                    matrix[i][j] = matrix[i][j-1]
                elif j == 0 and i != 0:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[-1][-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(1,2))


