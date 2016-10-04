"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        clean_first_column = False
        clean_first_row = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                clean_first_column = True
                break
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                clean_first_row = True
                break;

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    continue

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0

        if clean_first_row == True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if clean_first_column == True:
            for i in range(len(matrix)):
                matrix[i][0] = 0






