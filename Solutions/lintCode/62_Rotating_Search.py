# -*- coding: utf-8 -*-
# @Time     : 2021/12/27 16:18
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 62_Rotating_Search.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A: list, target: int) -> int:
        # write your code here
        if len(A) == 0:
            return -1
        top_index = len(A) - 1
        bottom_index = 0

        while True:
            index = (top_index + bottom_index) // 2
            try:
                print(f"A[{index}]: {A[index]}, A[{bottom_index}]: {A[bottom_index]}, A[{top_index}]: {A[top_index]}, target:{target}")
            except:
                pass
            if bottom_index > top_index:
                index = -1
                break
            elif target == A[index]:
                break
            elif A[index] > target:
                if A[index] < A[top_index] or target >= A[bottom_index]:
                    top_index = index - 1
                else:
                    bottom_index = index + 1

            elif A[index] < target:
                if A[index] > A[bottom_index] or target <= A[top_index]:
                    bottom_index = index + 1
                else:
                    top_index = index - 1
        print(index)
        return index


if __name__ == '__main__':
    s = Solution()
    As = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(20):
        s.search(As, i)

