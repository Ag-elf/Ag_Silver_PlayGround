# -*- coding: utf-8 -*-
# @Time     : 2021/12/21 15:42
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 719_Find_K-th_Smallest_Pair_Distance.py
# @Version  : Python 3.8.5 +
from typing import List


def get_count(distance, nums):
    count = 0
    j = 0
    for i in range(1, len(nums)):
        while nums[i] - nums[j] > distance:
            j += 1
        count += i - j
    return count


def smallestDistancePair(nums: List[int], k: int) -> int:
    nums.sort()
    left = 0
    right = nums[-1] - nums[0]
    while left < right:
        mid = (left + right) >> 1
        if get_count(mid, nums) < k:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    res = smallestDistancePair([1, 3, 6, 7, 11, 6, 12], 4)
    print(res)
