# -*- coding: utf-8 -*-
# @Time     : 2021/12/29 16:28
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 1995_Quadruplets.py
# @Version  : Python 3.8.5 +
from collections import Counter
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        counter = 0
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for n in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[n]:
                            counter += 1

        return counter


if __name__ == '__main__':
    raw = [28, 8, 49, 85, 37, 90, 20, 8]
    s = Solution()
    counter = s.countQuadruplets(raw)
    print(counter)
