# -*- coding: utf-8 -*-
# @Time     : 2021/12/24 16:38
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 680_Split_String.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s: str) -> list:
        # write your code here
        result = [[]]
        if len(s) == 1:
            result = [[s[0]]]
        elif len(s) != 0:
            result = []
            temp = self.splitString(s[:len(s)-1])
            for raw in temp:
                if len(raw[len(raw) - 1]) == 1:
                    new_raw = raw.copy()
                    new_raw.append(s[len(s) - 1])
                    raw[len(raw) - 1] += s[len(s) - 1]
                    result.append(raw)
                    result.append(new_raw)
                else:
                    raw.append(s[len(s) - 1])
                    result.append(raw)
        print(result)
        return result

    def splitString2(self, s: str) -> list:
        # dfs


        return


if __name__ == '__main__':
    k = Solution()
    k.splitString("12345")
