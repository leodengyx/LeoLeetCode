"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        count = 0
        total_count = n * n
        direction = 1  #Right
        row = 0
        column = 0
        result = [[None] * n] * n
        while count < total_count:
            result[row][column] = count + 1

            if 

            if direction == 0:  #Up
                row -= 1
            elif direction == 1:  #Right
                column += 1
            elif direction == 2:  #Down
                row += 1
            elif direction == 3:  #Left
                column -= 1
            count += 1




