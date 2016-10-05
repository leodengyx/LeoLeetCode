"""
Given a set of distinct integers, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        self.subsetsByRecur(nums, result, [], 0)
        return result

    def subsetsByRecur(self, nums, result, intermediate, index):
        while index <= len(nums) - 1:
            intermediate.append(nums[index])
            result.append(intermediate[:])
            self.subsetsByRecur(nums, result, intermediate, index+1)
            intermediate.pop(-1)
            index += 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3]))





