# -*- coding: utf-8 -*-
# @Time     : 2021/12/31 9:29
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 848_Basic_Calculator.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param s: the expression string
    @return: the answer
    """

    def __init__(self):
        self.index = 0

    def calculate(self, s: str) -> int:
        # Write your code here
        result = []
        ops = ""
        num = 0
        while self.index < len(s) and s[self.index] != ')':
            print("=" * 10)
            print(s[self.index])
            if s[self.index] in '+-*/':
                ops = s[self.index]
                self.index += 1

            if s[self.index] == ' ':
                self.index += 1
                continue

            elif s[self.index].isdigit():
                while self.index < len(s) and s[self.index].isdigit():
                    num = num * 10 + int(s[self.index])
                    self.index += 1

            elif s[self.index] == '(':
                self.index += 1
                num = self.calculate(s)
                self.index += 1
                print(f"++: {num}")
                print(self.index)

            print("BEFORE")
            print(self.index, num, ops, result)
            if self.index <= len(s) and ops != 'E':
                if ops == '+' or ops == '':
                    result.append(num)
                elif ops == '-':
                    result.append(-num)
                elif ops == '*':
                    result[-1] = result[-1] * num
                elif ops == '/':
                    result[-1] = abs(result[-1]) // abs(num) * (result[-1] // abs(result[-1])) * (num // abs(num))
                ops = 'E'
                num = 0
            print("AFTER")
            print(self.index, num, ops, result)

        return sum(result)


if __name__ == '__main__':
    strs = "1 + (2 + 3) * 3"
    ss = Solution()
    print(ss.calculate(strs))