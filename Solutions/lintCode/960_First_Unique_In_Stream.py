# -*- coding: utf-8 -*-
# @Time     : 2021/12/23 14:55
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 960_First_Unique_In_Stream.py
# @Version  : Python 3.8.5 +
class DataStream:

    def __init__(self):
        self.dicts = {}
        self.k = {}
        pass

    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):
        if self.k.get(num) is not None:
            return
        if self.dicts.get(num) is None:
            self.dicts[num] = 1
        else:
            self.dicts.pop(num)
            self.k[num] = 1

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):
        for k, v in self.dicts.items():
            print(k)
            return k


if __name__ == '__main__':
    ds = DataStream()
    ds.add(1)
    ds.add(1)
    ds.add(2)
    ds.add(2)
    ds.add(1)
    ds.add(3)
    ds.firstUnique()
