"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import sys

class Solution(object):

    '''
    Solution 1: Brutal Force
    '''
    def threeSumClosest_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        absolute_delta = sys.maxint
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == target:
                        return target
                    elif nums[i]+nums[j]+nums[k] > target and nums[i]+nums[j]+nums[k] - target < absolute_delta:
                        absolute_delta = nums[i]+nums[j]+nums[k] - target
                        closest_value = nums[i]+nums[j]+nums[k]
                    elif nums[i]+nums[j]+nums[k] < target and target - (nums[i]+nums[j]+nums[k]) < absolute_delta:
                        absolute_delta = target - (nums[i]+nums[j]+nums[k])
                        closest_value = nums[i]+nums[j]+nums[k]
        return closest_value

    '''
    Solutions: Based on 2Sum solution
    '''
    def threeSumClosest_2(self, nums, target):
        sorted_nums = sorted(nums)
        absolute_delta = sys.maxint
        for i in range(len(sorted_nums) - 2):
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                if sorted_nums[i]+sorted_nums[j]+sorted_nums[k] == target:
                    return target
                elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > target:
                    if sorted_nums[i]+sorted_nums[j]+sorted_nums[k] - target < absolute_delta:
                        absolute_delta = sorted_nums[i]+sorted_nums[j]+sorted_nums[k] - target
                        closest_value = sorted_nums[i]+sorted_nums[j]+sorted_nums[k]
                    k -= 1
                elif sorted_nums[i]+sorted_nums[j]+sorted_nums[k] < target:
                    if target - (sorted_nums[i]+sorted_nums[j]+sorted_nums[k]) < absolute_delta:
                        absolute_delta = target - (sorted_nums[i]+sorted_nums[j]+sorted_nums[k])
                        closest_value = sorted_nums[i]+sorted_nums[j]+sorted_nums[k]
                    j += 1
        return closest_value


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest_1([-1, 2, 1, -4], 1))
    print(solution.threeSumClosest_2([-1, 2, 1, -4], 1))








