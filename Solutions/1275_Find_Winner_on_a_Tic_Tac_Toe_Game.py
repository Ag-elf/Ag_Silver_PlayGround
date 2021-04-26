# -*- coding: utf-8 -*-
# @Time     : 2021/4/26 14:37
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 1275_Find_Winner_on_a_Tic_Tac_Toe_Game.py
# @Version  : Python 3.8.5 +
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) <= 4:
            return "Pending"
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(moves)):
            if i % 2 == 0:
                board[moves[i][0]][moves[i][1]] = 1
            else:
                board[moves[i][0]][moves[i][1]] = -1

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == -1:
                return 'B'
            elif board[i][0] == board[i][1] == board[i][2] == 1:
                return 'A'

            if board[0][i] == board[1][i] == board[2][i] == -1:
                return 'B'
            elif board[0][i] == board[1][i] == board[2][i] == 1:
                return 'A'

        if board[0][0] == board[1][1] == board[2][2] == -1:
            return 'B'
        elif board[0][0] == board[1][1] == board[2][2] == 1:
            return 'A'

        if board[2][0] == board[1][1] == board[0][2] == -1:
            return 'B'
        elif board[2][0] == board[1][1] == board[0][2] == 1:
            return 'A'

        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'


if __name__ == '__main__':
    mov = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    sol = Solution()
    print(sol.tictactoe(mov))
