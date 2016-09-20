"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
 which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
class Solution(object):

    '''
    Solution 1: Brutal Force
    '''
    def maxArea_1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                if (min(height[i], height[j]) * (j-i)) > max_area:
                    max_area = (min(height[i], height[j]) * (j-i))
        return max_area

    '''
    Solution 2: 2 Pointers
    '''
    def maxArea_2(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left<right:
            if (min(height[left], height[right]) * (right-left)) > max_area:
                max_area = (min(height[left], height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea_2([1,1]))