# -*- coding: utf-8 -*-
# @Time     : 2021/12/21 14:41
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 715_Range_Module.py
# @Version  : Python 3.8.5 +
import bisect


class RangeModule:

    def __init__(self):
        # ranges 首先一定是有序的
        self.ranges = []

    def __find_crossed(self, left: int, right: int):
        """
        找到所有相交的条件：
        1. ranges[left] <= target_right
        2. ranges[right] >= target_left
        :param left:
        :param right:
        :return:
        """
        i, j = 0, len(self.ranges) - 1

        while i <= len(self.ranges) - 1 and self.ranges[i][1] < left:
            i += 1

        while j >= i and self.ranges[j][0] > right:
            j -= 1

        return i, j

    def addRange(self, left: int, right: int) -> None:
        # 找到所有相交的数组
        i, j = self.__find_crossed(left, right)
        if i <= j:
            left = min(self.ranges[i][0], left)
            right = max(self.ranges[j][1], right)
        # 不论多少在一起，最终都会变成一个
        self.ranges[i: j + 1] = [(left, right)]

    def queryRange(self, left: int, right: int) -> bool:
        # 二分查找，找到 ranges[i], (i-1)_left < target_left < (i)_left
        # 如果要覆盖，则一定是 ranges[i-1] 与 target 覆盖
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if len(self.ranges) == 0:
            return False
        if self.ranges[i - 1][1] >= right and self.ranges[i - 1][0] <= left:
            return True
        else:
            return False

    def removeRange(self, left: int, right: int) -> None:
        # 找到所有相交的数组
        i, j = self.__find_crossed(left, right)
        if i <= j:
            merge = []
            # 如果 i_left < left, 则删除后 [i_left, left) 加入区间
            if self.ranges[i][0] < left:
                merge.append((self.ranges[i][0], left))

            # 如果 right < i_right, 则删除后 [right, i_right) 加入区间
            if self.ranges[j][1] > right:
                merge.append((right, self.ranges[j][1]))

            self.ranges[i: j + 1] = merge


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

if __name__ == '__main__':
    kk = RangeModule()
    kk.addRange(6, 8)
    print(kk.ranges)
    kk.removeRange(7, 8)
    print(kk.ranges)
    kk.removeRange(8, 9)
    print(kk.ranges)
    kk.addRange(8, 9)
    print(kk.ranges)
    kk.removeRange(1, 3)
    print(kk.ranges)
    kk.addRange(1, 8)
    print(kk.ranges)
    kk.queryRange(2, 4)
    kk.queryRange(2, 9)
    kk.queryRange(4, 6)

    # ["RangeModule", "addRange", "removeRange", "removeRange", "addRange", "removeRange", "addRange", "queryRange",
    #  "queryRange", "queryRange"]
    # [[], [6, 8], [7, 8], [8, 9], [8, 9], [1, 3], [1, 8], [2, 4], [2, 9], [4, 6]]
