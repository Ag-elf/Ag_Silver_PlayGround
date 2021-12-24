# -*- coding: utf-8 -*-
# @Time     : 2021/12/24 16:26
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 702_Concatenate_String.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        a1 = set(s1)
        a2 = set(s2)
        res = a1.intersection(a2)
        for c in res:
            s1 = s1.replace(c, "")
            s2 = s2.replace(c, "")
            print(s1, s2, c)
        result = s1 + s2
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.concatenetedString("abcdc", "efgd")
    print(res)