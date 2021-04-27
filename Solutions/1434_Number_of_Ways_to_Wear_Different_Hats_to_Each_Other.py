# -*- coding: utf-8 -*-
# @Time     : 2021/04/27 11:12
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 1434_Number_of_Ways_to_Wear_Different_Hats_to_Each_Other.py
# @Version  : Python 3.8.5 +
from typing import List


"""
There are n people and 40 types of hats labeled from 1 to 40.

Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:

1. n == hats.length
2. 1 <= n <= 10
3. 1 <= hats[i].length <= 40
4. 1 <= hats[i][j] <= 40
5. hats[i] contains a list of unique integers.

"""


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        return 1

if __name__ == "main":
    input = []
    sol = Solution()
    ans = sol.numberWays(input)
