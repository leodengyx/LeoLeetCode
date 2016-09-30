"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left_height_list = [None] * len(height)
        max_right_height_list = [None] * len(height)
        max_left_height = None
        max_right_height = None
        for i in range(len(height)):
            if max_left_height is None:
                max_left_height = height[i]
                max_left_height_list[i] = max_left_height
            elif max_left_height >= height[i]:
                max_left_height_list[i] = max_left_height
            elif max_left_height < height[i]:
                max_left_height_list[i] = max_left_height
                max_left_height = height[i]

            if max_right_height is None:
                max_right_height = height[len(height) - i - 1]
                max_right_height_list[len(height) - i - 1] = max_right_height
            elif max_right_height >= height[len(height) - i - 1]:
                max_right_height_list[len(height) - i - 1] = max_right_height
            elif max_right_height < height[len(height) - i - 1]:
                max_right_height_list[len(height) - i - 1] = max_right_height
                max_right_height = height[len(height) - i - 1]

        result = 0
        for i in range(len(height)):
            if max_right_height_list[i] > 0 and max_left_height_list[i] > 0 and min(max_left_height_list[i], max_right_height_list[i]) > height[i]:
                result += min(max_left_height_list[i], max_right_height_list[i]) - height[i]
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
