"""
合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None:
            return
        ls = len(intervals)
        if ls <= 1:
            return intervals
        # sort by start
        intervals.sort(key=lambda x: x[0])
        print("sorted", intervals)
        pos = 0
        while pos < len(intervals) - 1:
            # check overlap
            if intervals[pos][-1] >= intervals[pos + 1][0]:
                next = intervals.pop(pos + 1)
                # check next is overlap or totally covered by pos
                if next[-1] > intervals[pos][-1]:
                    intervals[pos][-1] = next[-1]
            # print [(t.start, t.end) for t in intervals], pos
            else:
                pos += 1
        return intervals

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.merge([[1,3],[2, 6],[8, 10],[15,18]]))
    print(s.merge([[1, 4], [4, 5]]))