# coding=utf-8
"""
Implement next permutation(排列), which rearranges numbers into the lexicographically（字典顺序） next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break;
            else:
                i -= 1
        if i == -1:
            for j in range(len(nums) / 2):
                nums[j], nums[len(nums) - j - 1] = nums[len(nums) - j - 1], nums[j]
        else:
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break;
            j = i+1
            k = len(nums) - 1
            while j < k:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1
                k -= 1
        return nums

if __name__ == "__main__":
    solution = Solution()
    print(solution.nextPermutation([1,3,2]))


