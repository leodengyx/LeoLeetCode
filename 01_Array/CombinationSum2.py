"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = {}
        self.combinationSum2ByRecur(sorted(candidates), result, 0, [], target)
        return result.values()

    def combinationSum2ByRecur(self, candidates, result, start, intermediate, target):
        if target == 0:
            if result.get(str(list(intermediate))) is None:
                result[str(list(intermediate))] = list(intermediate)
        while start < len(candidates) and target >= candidates[start]:
            intermediate.append(candidates[start])
            self.combinationSum2ByRecur(candidates, result, start + 1, intermediate, target - candidates[start])
            intermediate.pop()
            start += 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))


