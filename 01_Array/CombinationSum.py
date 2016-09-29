"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSumByRecur(sorted(candidates), result, 0, [], target)
        return result

    def combinationSumByRecur(self, candidates, result, start, intermediate, target):
        #print("start=%d, intermediate=%s, target=%d, result=%s" % (start, str(intermediate), target, str(result)))
        if target == 0:
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            self.combinationSumByRecur(candidates, result, start, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))





