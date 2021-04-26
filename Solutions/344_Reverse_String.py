# -*- coding: utf-8 -*-
# @Time     : 2021/4/26 14:09
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 344_Reverse_String.py
# @Version  : Python 3.8.5 +

"""
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stt = 0
        end = len(s) - 1

        while stt < end:
            temp = s[stt]
            s[stt] = s[end]
            s[end] = temp
            stt += 1
            end -= 1
        print(s)
        return

if __name__ == '__main__':
    sol = Solution()
    strs = [""]
    sol.reverseString(strs)
