"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

!!!
Pay attention:
can be integers less than zero;
2 elements can be the same
!!!
"""


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pass

    '''
    Solution 1 - Brutal Force
    Complexity: O(n^2)
    '''
    def twoSum_1(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]

    '''
    Solution 2 - Use assist array. First round scan the input array and mark each element's partner location in
     assist array. Second round scan the assist array to see each element whether have valid partner.
    Complexity: O(2n)
    !!! This method can't accept integer less than 0 !!!

    def twoSum_2(self, nums, target):
        assistArray = [None] * (target+1)
        for i in range(len(nums)):
            if nums[i] <= target:
                assistArray[nums[i]] = target - nums[i]
        first = -1
        second = -1
        for i in range(len(nums)):
            if first == -1 and nums[i] <= target and assistArray[nums[i]] is not None and assistArray[nums[i]] != nums[i]:
                first = i
            if first != -1 and nums[i] == assistArray[nums[first]]:
                second = i
                return [first, second]
    '''

    '''
    Approach #2 (Two-pass Hash Table)
    To improve our run time complexity, we need a more efficient way to check if the complement exists in the array.
    If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element
    in the array to its index? A hash table.

    We reduce the look up time from O(n) to O(1) by trading space for speed. A hash table is built exactly
    for this purpose, it supports fast look up in near constant time. I say "near" because if a collision occurred,
    a look up could degenerate to O(n) time. But look up in hash table should be amortized O(1) time as long
    as the hash function was chosen carefully.

    A simple implementation uses two iterations. In the first iteration, we add each element's value and its index
    to the table. Then, in the second iteration we check if each element's complement (target - nums[i])
    exists in the table. Beware that the complement must not be nums[i] itself!
    '''
    def twoSum_2(self, nums, target):
        value_index_dict = {}
        for i in range(len(nums)):
            if value_index_dict.get(nums[i]) is None:
                value_index_dict[nums[i]] = [i]
            else:
                value_index_dict[nums[i]].append(i)
        for i in range(len(nums)):
            if value_index_dict.get(target - nums[i]) is not None:
                if target - nums[i] != nums[i]:
                    return [value_index_dict[nums[i]][0], value_index_dict[target - nums[i]][0]]
                elif target - nums[i] == nums[i] and len(value_index_dict[nums[i]]) == 2:
                    return value_index_dict[nums[i]]

    '''
    Approach #3 (One-pass Hash Table)
    It turns out we can do it in one-pass. While we iterate and inserting elements into the table, we also look back
     to check if current element's complement already exists in the table. If it exists, we have found a solution and
     return immediately.
    '''
    def twoSum_3(self, nums, target):
        value_index_dict = {}
        for i in range(len(nums)):
            if value_index_dict.get(nums[i]) is None:

                if value_index_dict.get(target - nums[i]) is not None:
                    return [value_index_dict[target - nums[i]], i]

                value_index_dict[nums[i]] = i
            elif value_index_dict.get(nums[i]) is not None and nums[i] == target - nums[i]:
                return [value_index_dict[target - nums[i]], i]

if __name__ == "__main__":
    solution = Solution();
    print(solution.twoSum_1([2, 7, 11, 15], 9))
    print(solution.twoSum_3([0, 4, 3 , 0], 0))