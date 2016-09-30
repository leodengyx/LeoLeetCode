"""
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.
"""
import sys


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for j in range(len(nums)):
            if nums[j] != j + 1:
                return j + 1
        return len(nums) + 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([9,4,-1,2]))



