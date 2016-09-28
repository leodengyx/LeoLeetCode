# coding=utf-8
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[left] > target:
                index = left
                break
            elif nums[right] < target:
                index = right + 1
                break
            elif nums[mid] < target and nums[right] >= target:
                if mid != right:
                    left = mid + 1
                    index = left
                else:
                    index = right
                    break
            elif nums[mid] > target and nums[left] <= target:
                if mid != left:
                    right = mid - 1
                    index = right
                else:
                    index = left
                    break
        return index

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,3,5,6], 5))
    print(solution.searchInsert([1,3,5,6], 2))
    print(solution.searchInsert([1,3,5,6], 7))
    print(solution.searchInsert([1,3,5,6], 0))