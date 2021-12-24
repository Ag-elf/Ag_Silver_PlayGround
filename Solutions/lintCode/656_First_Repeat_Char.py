# -*- coding: utf-8 -*-
# @Time     : 2021/12/23 14:41
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 656_First_Repeat_Char.py
# @Version  : Python 3.8.5 +
class Solution:
    """
    @param s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        temp = {}
        for i in range(len(s)):
            if temp.get(s[i]) is None:
                temp[s[i]] = i
            else:
                temp[s[i]] = -1
        for k, v in temp.items():
            if v != -1:
                return v
        return -1


if __name__ == '__main__':
    raw = "rstvsadsfdasfdasfadsfdasfrtbv"
    s = Solution()
    print(s.firstUniqChar(raw))
