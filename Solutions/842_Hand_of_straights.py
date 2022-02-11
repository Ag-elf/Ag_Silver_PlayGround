# -*- coding: utf-8 -*-
# @Time     : 2021/12/30 16:33
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 842_Hand_of_straights.py
# @Version  : Python 3.8.5 +
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        elif groupSize == 1:
            return True
        result = Counter(hand)
        key_list = [k for k in result.keys()]
        key_list.sort()

        for key in key_list:
            if result[key] > 0:
                card_counts = result[key]
                for i in range(groupSize):
                    if result.get(key + i) is None:
                        return False
                    else:
                        result[key + i] -= card_counts
            elif result[key] < 0:
                return False
        return True


if __name__ == '__main__':
    hands = [1, 2, 3, 4, 5, 6]
    s = Solution()
    res = s.isNStraightHand(hands, 3)
    print(res)
