# -*- coding: utf-8 -*-
# @Time     : 2021/12/24 15:29
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 1250_3rd_largest.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param nums: the array
    @return: the third maximum number in this array
    """
    def thirdMax(self, nums):
        max_arr =[]
        for num in nums:
            if num in max_arr:
                continue
            elif len(max_arr) < 3:
                max_arr.append(num)
            else:
                if num > min(max_arr):
                    max_arr.remove(min(max_arr))
                    max_arr.append(num)

        if len(max_arr) < 3:
            return max(max_arr)
        else:
            return min(max_arr)


if __name__ == '__main__':
    s = Solution()
    res = s.thirdMax([1, 2, 2, 3])
    print(res)
