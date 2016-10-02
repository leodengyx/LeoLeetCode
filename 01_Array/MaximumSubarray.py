"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
click to show more practice.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_add_result_list = [None] * len(nums)
        result = None
        for i in range(len(nums)):
            if i == 0:
                max_add_result_list[i] = nums[i]
                result = nums[i]
            else:
                max_add_result_list[i] = max(nums[i], max_add_result_list[i-1] + nums[i])
                if result < max_add_result_list[i]:
                    result = max_add_result_list[i]
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,-1]))

