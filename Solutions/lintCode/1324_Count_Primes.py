# -*- coding: utf-8 -*-
# @Time     : 2021/12/24 17:18
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 1324_Count_Primes.py
# @Version  : Python 3.8.5 +
import math


class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        if n <= 1:
            return 0
        not_prime = [False] * n
        count = 0
        for i in range(2, n):
            if not not_prime[i]:
                count += 1
                for j in range(2, n):
                    if i * j >= n:
                        break
                    not_prime[j * i] = True

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))