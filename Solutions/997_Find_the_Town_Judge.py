# -*- coding: utf-8 -*-
# @Time     : 2021/04/27 10:53
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 997_Find_the_Town_Judge.py
# @Version  : Python 3.8.5 +

"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""
from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted_list = [0] * N
        trust_list = [0] * N
        for i in range(len(trust)):
            a = trust[i][0]
            b = trust[i][1]
            trust_list[a] += 1
            trusted_list[b] += 1

        for i in range(N):
            if trusted_list[i] == N - 1 and trust_list[i] == 0:
                return i + 1
        return -1
