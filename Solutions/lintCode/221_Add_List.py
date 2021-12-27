# -*- coding: utf-8 -*-
# @Time     : 2021/12/27 18:04
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 221_Add_List.py
# @Version  : Python 3.8.5 +

class ListNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        temp = self.next
        val = f"{self.val}"
        while temp is not None:
            val += str(temp.val)
            temp = temp.next
        return val

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def reverse(self, node: ListNode):
        temp = node
        raw = None
        while temp is not None:
            next_node = temp.next
            temp.next = raw
            raw = temp
            temp = next_node
        return raw

    def addLists2(self, l1, l2):
        # write your code here
        r_l1 = self.reverse(l1)
        r_l2 = self.reverse(l2)
        while True:
            pass
        pass


if __name__ == '__main__':
    A = [1, 2, 3]
    B = [2, 3, 4, 5]

    a = None
    for i in range(len(A)):
        n = ListNode(A[len(A) - 1 - i], a)
        a = n

    b = None
    for i in range(len(B)):
        n = ListNode(B[len(B) - 1 - i], b)
        b = n

    s = Solution()
    print(a)
    print(s.reverse(a))
    print(b)
    print(s.reverse(b))