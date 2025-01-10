"""
    Given a collection of intervals, find the minimum number of intervals you 
    need to remove to make the rest of the intervals non-overlapping.

    Example:
    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are 
                 non-overlapping.

    Example:
    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals 
                 non-overlapping.

    Example:
    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're 
                 already non-overlapping.

    Note:
        1. You may assume the interval's end point is always bigger than its 
           start point.
        2. Intervals like [1,2] and [2,3] have borders "touching" but they 
           don't overlap each other.
"""
#Difficulty: Medium
#18 / 18 test cases passed.
#Runtime: 72 ms
#Memory Usage: 17 MB

#Runtime: 72 ms, faster than 84.83% of Python3 online submissions for Non-overlapping Intervals.
#Memory Usage: 17 MB, less than 42.34% of Python3 online submissions for Non-overlapping Intervals.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        overlap = 0
        length = len(intervals)
        intervals.sort(key=lambda intervals : intervals[1])
        while True:
            j = i + 1
            if j >= length:
                return overlap
            if intervals[j][0] < intervals[i][1]:
                overlap += 1
                intervals.pop(j)
                i -= 1
                length -= 1
            i += 1
