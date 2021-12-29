# -*- coding: utf-8 -*-
# @Time     : 2021/12/29 15:04
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 1944_Visible_People.py
# @Version  : Python 3.8.5 +
from typing import List


class Solution:
    def canSeePersonsCount2(self, heights: List[int]) -> List[int]:
        stack = []
        result = []
        result_arr = [0] * len(heights)
        for i in range(len(heights)):
            # print(stack)
            data = [i, 0]
            if len(stack) == 0:
                stack.append(data)
                continue

            index = stack[len(stack) - 1][0]
            if heights[index] > heights[i]:
                stack[len(stack) - 1][1] += 1
                stack.append(data)
            else:
                while heights[index] < heights[i]:
                    stack[len(stack) - 1][1] += 1
                    result.append(stack.pop())
                    if len(stack) != 0:
                        index = stack[len(stack) - 1][0]
                    else:
                        break
                if len(stack) != 0:
                    stack[len(stack) - 1][1] += 1
                stack.append(data)

        for rs in result:
            result_arr[rs[0]] = rs[1]

        for rs in stack:
            result_arr[rs[0]] = rs[1]

        return result_arr

    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        result = [0] * len(heights)
        for i in range(len(heights)):
            now_heights = heights[len(heights) - 1 - i]
            if len(stack) == 0:
                stack.append(now_heights)
            else:
                while len(stack) != 0 and now_heights > stack[-1]:
                    result[len(heights) - 1 - i] += 1
                    stack.pop()
                if len(stack) != 0:
                    result[len(heights) - 1 - i] += 1
                stack.append(now_heights)
        return result


if __name__ == '__main__':
    heights = [10, 6, 8, 5, 11, 9]
    s = Solution()
    res = s.canSeePersonsCount(heights)
    print(res)
