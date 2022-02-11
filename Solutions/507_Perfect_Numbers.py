# -*- coding: utf-8 -*-
# @Time     : 2021/12/31 10:44
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 507_Perfect_Numbers.py
# @Version  : Python 3.8.5 +
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sums = 1
        for i in range(2, math.floor(math.sqrt(num) + 1)):
            if num % i == 0:
                print(i)
                sums += i
                sums += num // i
        if sums == num:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    res = s.checkPerfectNumber(6)
    print(res)
