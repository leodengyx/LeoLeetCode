"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):

    """
    Solution 1: Brutal Force
    """
    def threeSum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_dict = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if not (i == j or i == k or j == k):
                        if nums[i] + nums[j] + nums[k] == 0:
                            result_dict[str(sorted([nums[i], nums[j], nums[k]]))] = sorted([nums[i], nums[j], nums[k]])
        return result_dict.values()

    """
    Solution 2: Based on 2Sum solution
    """
    def threeSum_2(self, nums):
        result_dict = {}
        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            value_index_dict = {}
            for j in range(i+1, len(nums)):
                if value_index_dict.get(target - nums[j]) is not None:
                    result_dict[str(sorted([nums[i], nums[j], target-nums[j]]))] = sorted([nums[i], nums[j], target-nums[j]])
                value_index_dict[nums[j]] = j
        return result_dict.values()

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum_1([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum_2([-1, 0, 1, 2, -1, -4]))



