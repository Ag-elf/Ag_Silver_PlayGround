# -*- coding: utf-8 -*-
# @Time     : 2021/04/27 10:06
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 341_Flatten_Nested_List_Iterator.py
# @Version  : Python 3.8.5 +

"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

1. NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
2. int next() Returns the next integer in the nested list.
3. boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
"""

class NestedInteger:

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.real_list = []
        self.real_list = self.getList(nestedList)
        self.index = 0
        self.length = len(self.real_list)
    
    def next(self) -> int:
        self.index += 1
        return self.real_list[self.index - 1]
    
    def hasNext(self) -> bool:
        if self.index >= self.length:
            return False
        else:
            return True
    
    def getList(self, nest_integer: [NestedInteger]) -> list:
        int_list = []
        # print(nest_integer)
        for integer in nest_integer:
            if integer.isInteger():
                int_list.append(integer.getInteger())
            else:
                n_int = integer.getList()
                int_list += self.getList(n_int)
        
        return int_list
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
