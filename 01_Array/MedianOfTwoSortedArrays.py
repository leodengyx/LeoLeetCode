"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1+len2)%2 == 1:
            return self.getkth(nums1, nums2, (len1+len2)/2 + 1)
        else:
            return (self.getkth(nums1, nums2, (len1+len2)/2) + self.getkth(nums1, nums2, (len1+len2)/2+1)) * 0.5

    def getkth(self, a, b, k):
        m = len(a)
        n = len(b)
        if m > n:
            return self.getkth(b, a, k)

        if m == 0:
            return b[k-1]
        if n == 0:
            return a[k-1]
        if k <= 1:
            return min(a[0], b[0])


        if m/2 + n/2 >= k:
            if a[m/2] > b[n/2]:
                if m > 1:
                    return self.getkth(a[m/2+1:], b, k-m/2)
                else:
                    return self.getkth([], b, k-1)
            else:
                if n > 1:
                    return self.getkth(a, b[n/2+1:], k-n/2)
                else:
                    return self.getkth(a, [], k-1)
        else:
            if a[m/2] > b[n/2]:
                if m > 1:
                    return self.getkth(a[:m/2], b, k-m/2)
                else:
                    return self.getkth([], b, k-1)
            else:
                if n > 1:
                    return self.getkth(a, b[:n/2], k-n/2)
                else:
                    return self.getkth(a, [], k-1)



if __name__ == "__main__":
    solution = Solution()
    print solution.findMedianSortedArrays([1,3], [2])
