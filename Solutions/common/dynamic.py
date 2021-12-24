# -*- coding: utf-8 -*-
# @Time     : 2021/12/23 16:29
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : dynamic.py
# @Version  : Python 3.8.5 +

def _0_1_packing(capacity: int, items: list) -> int:
    temp = [0] * capacity
    result = []
    for i in range(len(items) + 1):
        result.append(temp.copy())

    for i in range(1, len(items) + 1):
        for j in range(capacity):
            if j - items[i - 1][0] < 0:
                result[i][j] = result[i - 1][j]
            else:
                result[i][j] = max(result[i - 1][j - items[i - 1][0]] + items[i - 1][1], result[i - 1][j])

    for k in result:
        print(k)

    return result[-1][-1]


if __name__ == '__main__':
    packing = [
        [2, 3],
        [2, 4],
        [3, 4],
        [5, 6],
        [2, 7]
    ]
    print(_0_1_packing(8, packing))
