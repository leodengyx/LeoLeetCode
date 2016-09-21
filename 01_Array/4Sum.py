"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):

    '''
    Solution 1: Based on 3Sum but complexity is O(n^3)
    '''
    def fourSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_dict = {}
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                value_index_dict = {}
                for k in range(j+1, len(nums)):
                    if value_index_dict.get(target - nums[i] - nums[j] - nums[k]) is not None:
                        result_dict[str(sorted([nums[i], nums[j], nums[k], target - nums[i] - nums[j] - nums[k]]))] = \
                            sorted([nums[i], nums[j], nums[k], target - nums[i] - nums[j] - nums[k]])
                    if value_index_dict.get(nums[k]) is None:
                        value_index_dict[nums[k]] = k
        return result_dict.values()

    '''
    Solution 2: Based on 3Sum but complexity is O(n^2)
    '''
    def fourSum_2(self, nums, target):
        result_dict = {}
        sorted_nums = sorted(nums)
        pair_sum = {}
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if pair_sum.get(nums[i] + nums[j]) is None:
                    pair_sum[nums[i] + nums[j]] = []
                pair_sum[nums[i] + nums[j]].append([i, j])
        for first_pair_sum in pair_sum.keys():
            second_pair_sum = target - first_pair_sum
            if pair_sum.get(second_pair_sum) is not None:
                for [a,b] in pair_sum[first_pair_sum]:
                    for [c,d] in pair_sum[second_pair_sum]:
                        if a!=c and a!=d and b!=c and b!=d:
                            if result_dict.get(str(sorted([nums[a], nums[b], nums[c], nums[d]]))) is None:
                                result_dict[str(sorted([nums[a], nums[b], nums[c], nums[d]]))] = sorted([nums[a], nums[b], nums[c], nums[d]])
        return result_dict.values()

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum_1([1, 0, -1, 0, -2, 2], 0))
    print(solution.fourSum_2([1, 0, -1, 0, -2, 2], 0))





