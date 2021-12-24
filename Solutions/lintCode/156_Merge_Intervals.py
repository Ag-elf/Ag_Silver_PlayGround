# -*- coding: utf-8 -*-
# @Time     : 2021/12/23 14:01
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 156_Merge_Intervals.py
# @Version  : Python 3.8.5 +

from functools import cmp_to_key
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """

    def __init__(self):
        pass

    def __compare(self, a, b):
        if a.start > b.start:
            return 1
        elif a.start < b.start:
            return -1
        else:
            return 0

    def __find_interval(self, intervals, target: 'Interval'):
        i, j = 0, len(intervals) - 1

        while i <= len(intervals) - 1 and intervals[i].end < target.start:
            i += 1

        while j >= i and intervals[j].start > target.end:
            j -= 1

        return i, j

    # Consider the
    def merge2(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start > result[-1].end:
                result.append(interval)
            else:
                result[-1].end = max(interval.end, result[-1].end)

        return result

    # Origin Solution, slow and redundant
    def merge(self, intervals):
        intervals.sort(key=cmp_to_key(self.__compare))
        result_intervals = []
        for inter in intervals:
            if len(result_intervals) == 0:
                result_intervals.append(inter)
                continue

            i, j = self.__find_interval(result_intervals, inter)
            if i <= j:
                left = min(result_intervals[i].start, inter.start)
                right = max(result_intervals[j].end, inter.end)
                result_intervals[i: j+1] = [Interval(left, right)]

            else:
                result_intervals.append(inter)
        return result_intervals


if __name__ == '__main__':
    raw = [(1, 3), (4, 5), (2, 8)]
    prep = []
    for inter in raw:
        prep.append(Interval(inter[0], inter[1]))

    ee = Solution()
    res = ee.merge2(prep)
    for inter in res:
        print(inter.start, inter.end)
