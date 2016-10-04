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
        cur_row = 0
        cur_column = 0
        start_row = 0
        end_row = n - 1
        start_column = 0
        end_column = n - 1
        result = []
        for i in range(n):
           result.append([None] * n)
        while count < total_count:
            result[cur_row][cur_column] = count + 1

            if count != 0:
                if cur_row == start_row and cur_column == end_column:
                    direction = 2
                elif cur_column == end_column and cur_row == end_row:
                    direction = 3
                elif cur_row == end_row and cur_column == start_column:
                    direction = 0
                elif cur_column == start_column and cur_row == start_row + 1:
                    start_row += 1
                    end_row -= 1
                    start_column += 1
                    end_column -= 1
                    direction = 1

            if direction == 0:  #Up
                cur_row -= 1
            elif direction == 1:  #Right
                cur_column += 1
            elif direction == 2:  #Down
                cur_row += 1
            elif direction == 3:  #Left
                cur_column -= 1

            count += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(4))




