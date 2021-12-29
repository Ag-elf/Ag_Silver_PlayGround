# -*- coding: utf-8 -*-
# @Time     : 2021/12/27 18:04
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 221_Add_List.py
# @Version  : Python 3.8.5 +

class ListNode(object):
    def __init__(self, val, next=None):
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
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        r_l1 = self.reverse(l1)
        r_l2 = self.reverse(l2)
        plus = 0
        previous_node = None
        while r_l1 is not None or r_l2 is not None or plus != 0:
            if r_l1 is None:
                val_1 = 0
            else:
                val_1 = r_l1.val
                r_l1 = r_l1.next
            if r_l2 is None:
                val_2 = 0
            else:
                val_2 = r_l2.val
                r_l2 = r_l2.next
            sums = val_1 + val_2 + plus
            value = sums % 10
            plus = sums // 10
            now_node = ListNode(value, previous_node)
            previous_node = now_node

        return previous_node


if __name__ == '__main__':
    A = [1, 9]
    B = [9, 1]

    a = None
    for i in range(len(A)):
        n = ListNode(A[len(A) - 1 - i], a)
        a = n

    b = None
    for i in range(len(B)):
        n = ListNode(B[len(B) - 1 - i], b)
        b = n

    s = Solution()
    r = s.addLists2(a, b)
    print(r)
