"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        result = []
        start_column_index = 0
        end_column_index = len(matrix[0]) - 1
        start_row_index = 0
        end_row_index = len(matrix) - 1
        while end_row_index >= start_row_index and end_column_index >= start_column_index:
            if start_row_index == end_row_index and start_column_index == end_column_index:
                result.append(matrix[start_row_index][start_column_index])
                return result
            if start_row_index == end_row_index:
                for cur_column_index in range(start_column_index, end_column_index + 1):
                    result.append(matrix[start_row_index][cur_column_index])
                return result
            if start_column_index == end_column_index:
                for cur_row_index in range(start_row_index, end_row_index + 1):
                    result.append(matrix[cur_row_index][start_column_index])
                return result

            cur_row_index = start_row_index
            for cur_column_index in range(start_column_index, end_column_index):
                result.append(matrix[cur_row_index][cur_column_index])
            cur_column_index = end_column_index
            for cur_row_index in range(start_row_index, end_row_index):
                result.append(matrix[cur_row_index][cur_column_index])
            cur_row_index = end_row_index
            for cur_column_index in range(end_column_index, start_column_index, -1):
                result.append(matrix[cur_row_index][cur_column_index])
            cur_column_index = start_column_index
            for cur_row_index in range(end_row_index, start_row_index, -1):
                result.append(matrix[cur_row_index][cur_column_index])

            if start_row_index != end_row_index:
                start_row_index += 1
                end_row_index -= 1
            if start_column_index != end_column_index:
                start_column_index += 1
                end_column_index -= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder([[2,3]]))








