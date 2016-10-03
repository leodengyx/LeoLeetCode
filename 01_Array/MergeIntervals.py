"""
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


def getKey(item):
    return item.start

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=getKey)
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1].start <= intervals[i].start <= result[-1].end:
                result[-1].start = min(result[-1].start, intervals[i].start)
                result[-1].end = max(result[-1].end, intervals[i].end)
            else:
                result.append(intervals[i])
        return result

if __name__ == "__main__":
    solution = Solution()
    solution.merge()




