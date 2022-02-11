# -*- coding: utf-8 -*-
# @Time     : 2022/2/9 17:58
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : test.py
# @Version  : Python 3.8.5 +

class Solution:

    def countNum(self, m: int, n: int, k: int) -> int:
        sums = 0
        for i in range(m):
            sums += min(k // m, n)

        return sums

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        target = m * n // 2
        MAX = m * n
        MIN = 1

        while MIN < target:
            counter = self.countNum(m, n, target)
            print(MIN, target, MAX, counter)
            if counter > k:
                MAX = target
                target = (target + MIN) // 2
            elif counter < k:
                MIN = target
                target = (target + MAX) // 2
            else:
                return target

        return MIN


if __name__ == '__main__':
    s = Solution()
    s.findKthNumber(3, 3, 5)