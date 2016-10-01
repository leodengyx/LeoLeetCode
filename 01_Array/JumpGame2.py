"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
Note:
You can assume that you can always reach the last index.
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_step_list = [None] * len(nums)
        min_step_list[0] = 0
        for i in range(len(nums)):
            for j in range(i, i+nums[i]+1):
                if j >= len(nums):
                    break
                if min_step_list[j] is None or min_step_list[j] > min_step_list[i] + 1:
                    min_step_list[j] = min_step_list[i] + 1
                if j == len(nums) - 1:
                    return min_step_list[j]
                if j + nums[j] >= len(nums) - 1:
                    return min_step_list[j] + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.jump([2,3,1,1,4]))




        