# -*- coding: utf-8 -*-
# @Time     : 2021/12/27 14:55
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : play_ground.py
# @Version  : Python 3.8.5 +

def refresh(num: list, pos):
    if pos < 0 or num[0] == 16 - len(num):
        return False
    # print("+" * 10, pos)
    num[pos] += 1
    if num[pos] == 16 - (len(num) - pos - 1):
        # print("=" * 10, pos)
        refresh(num, pos - 1)
        num[pos] = num[pos - 1] + 1
    return True


def run():
    counter = [i for i in range(9)]
    flag = True

    one_line = 0
    two_line = 0
    three_line = 0
    total_counter = 0
    while flag:
        result_lines = 0
        data_base = [[0 for i in range(4)] for i in range(4)]
        # print(counter)
        for k in range(len(counter)):
            i = counter[k] // 4
            j = counter[k] % 4
            data_base[i][j] = 1

        # for lists in data_base:
        #     print(lists)

        ct_3 = 0
        ct_4 = 0
        for i in range(4):
            ct_1 = sum(data_base[i])
            ct_2 = data_base[0][i] + data_base[1][i] + data_base[2][i] + data_base[3][i]
            ct_3 += data_base[i][3 - i]
            ct_4 += data_base[i][i]
            # print(ct_1, ct_2, ct_3, ct_4)
            if ct_1 == 4:
                result_lines += 1

            if ct_2 == 4:
                result_lines += 1
        if ct_3 == 4:
            result_lines += 1

        if ct_4 == 4:
            result_lines += 1

        if result_lines == 1:
            one_line += 1
        elif result_lines == 2:
            # print("=" * 10)
            # for lists in data_base:
            #     print(lists)
            two_line += 1
        elif result_lines == 3:
            three_line += 1

        total_counter += 1

        # for lists in data_base:
        #     print(lists)
        flag = refresh(counter, len(counter) - 1)
        # print(result_lines)
    print(f"TOTAL: {total_counter}")
    print(f"One: {one_line}, {round(one_line/total_counter * 100, 2)} %")
    print(f"Two: {two_line}, {round(two_line/total_counter * 100, 2)} %")
    print(f"Three: {three_line}, {round(three_line/total_counter * 100, 2)} %")
    pass


if __name__ == '__main__':
    run()
    p = 36 * 24 / 11440
    raw = (1 - (1 - p) ** 5)
    print(raw)
    exit()
