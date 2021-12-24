# -*- coding: utf-8 -*-
# @Time     : 2021/12/24 17:59
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 162_Matrix_Zeros.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """

    def setZeroes(self, matrix):
        # write your code here
        if len(matrix) == 0:
            return
        for i in range(len(matrix)):
            column_zero = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    column_zero = 1
                    for k in range(i):
                        matrix[k][j] = 0
                elif matrix[0][j] == 0:
                    matrix[i][j] = 0

            if column_zero == 1:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0