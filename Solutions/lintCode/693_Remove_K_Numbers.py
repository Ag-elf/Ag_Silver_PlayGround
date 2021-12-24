# -*- coding: utf-8 -*-
# @Time     : 2021/12/24 13:59
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 693_Remove_K_Numbers.py
# @Version  : Python 3.8.5 +
from collections import Counter


class Solution:
    """
    @param num: a number
    @param k: the k digits
    @return: the smallest number
    """

    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"

        del_counter = 0
        result_set = [int(num[0])]
        for i in range(1, len(num)):

            while len(result_set) != 0 and del_counter < k:
                b = result_set.pop()
                if b <= int(num[i]):
                    result_set.append(b)
                    break
                else:
                    del_counter += 1
            result_set.append(int(num[i]))

        while del_counter < k:
            result_set.pop()
            del_counter += 1

        ct = 1
        res = ""
        # print(result_set)
        for i in range(len(result_set)):
            res += ct * result_set[len(result_set) - 1 - i]
            ct *= 10
        return str(res)


if __name__ == '__main__':
    s = Solution()
    result = s.removeKdigits("10", 1)
    print(result)
