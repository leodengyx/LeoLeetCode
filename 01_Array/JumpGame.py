"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        max_reach_index = 0
        for i in range(len(nums) - 1):
            if i > max_reach_index:
                return False
            max_reach_index = max(max_reach_index, i+nums[i])
            if max_reach_index >= len(nums) - 1:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([0,2,3]))






