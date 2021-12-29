# -*- coding: utf-8 -*-
# @Time     : 2021/12/28 16:13
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 927_Reverse_Words.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param str: a string
    @return: return a string
    """

    def reverseWords2(self, raw: str):
        # write your code here
        str_list = raw.split(" ")
        for i in range(len(str_list) // 2):
            temp = str_list[i]
            str_list[i] = str_list[len(str_list) - i - 1]
            str_list[len(str_list) - i - 1] = temp

        result = ""
        for i in range(len(str_list)):
            result += str_list[i]
            if i != len(str_list) - 1:
                result += " "

        return result

    def reverseWords(self, raw: str):
        result = ""
        temp = ""
        for i in range(len(raw)):
            c = raw[i]
            if c != " ":
                temp += c
            else:
                result = " " + temp + result
                temp = ""
        result = temp + result
        return result


if __name__ == '__main__':
    kk = "abasdfas"
    s = Solution()
    res = s.reverseWords(kk)
    print(res)

