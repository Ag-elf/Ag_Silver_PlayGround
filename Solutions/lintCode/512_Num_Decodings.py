# -*- coding: utf-8 -*-
# @Time     : 2021/12/28 15:20
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 512_Num_Decodings.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        if len(s) == 0 or s[0] == '0':
            return 0

        result = [0] * len(s)
        result[0] = 1

        for i in range(1, len(s)):

            print(result, s[:i])
            num = s[i - 1] + s[i]
            if num[0] == "0":
                if num[1] == "0":
                    return 0
                else:
                    result[i] = result[i - 1]
            elif num[1] == "0":
                if int(num[0]) >= 3:
                    return 0
                else:
                    if i == 1:
                        result[i] = 1
                    else:
                        result[i] = result[i - 2]
            elif int(num) > 26:
                result[i] = result[i - 1]
            else:
                if i == 1:
                    result[i] = 2
                else:
                    result[i] = result[i - 1] + result[i - 2]
        print(result)
        return result[len(s) - 1]


if __name__ == '__main__':
    k = "245123"
    s = Solution()
    s.numDecodings(k)
