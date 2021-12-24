# -*- coding: utf-8 -*-
# @Time     : 2021/12/23 15:31
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : sorting.py
# @Version  : Python 3.8.5 +

def merge_sort(inputs: list) -> list:
    if len(inputs) == 1:
        return inputs
    elif len(inputs) == 2:
        if inputs[0] > inputs[1]:
            temp = inputs[1]
            inputs[1] = inputs[0]
            inputs[0] = temp
        return inputs

    mid = len(inputs) // 2
    list_a = merge_sort(inputs[0: mid])
    list_b = merge_sort(inputs[mid: len(inputs)])

    piv_a = 0
    piv_b = 0
    result_list = []
    while piv_a < len(list_a) or piv_b < len(list_b):
        if piv_a >= len(list_a):
            result_list.extend(list_b[piv_b:])
            break

        if piv_b >= len(list_b):
            result_list.extend(list_a[piv_a:])

        if list_a[piv_a] < list_b[piv_b]:
            result_list.append(list_a[piv_a])
            piv_a += 1
        else:
            result_list.append(list_b[piv_b])
            piv_b += 1
    return result_list


if __name__ == '__main__':
    target = [1, 3, 2, 7, 3, 8, 9, 11, 4]
    print(merge_sort(target))
