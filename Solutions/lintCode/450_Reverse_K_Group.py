# -*- coding: utf-8 -*-
# @Time     : 2021/12/28 17:32
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 450_Reverse_K_Group.py
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
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """

    def reverse(self, node):
        temp = node
        raw = None
        while temp is not None:
            next_node = temp.next
            temp.next = raw
            raw = temp
            temp = next_node
        return raw

    def reverseKGroup(self, head, k):
        # write your code here
        counter = 0
        pivot = head
        now_head = head
        previous_end = None
        root = head
        while pivot:
            counter += 1
            if counter == k:
                counter = 0
                temp = pivot.next
                pivot.next = None
                if previous_end is not None:
                    previous_end.next = self.reverse(now_head)
                else:
                    self.reverse(now_head)
                now_head.next = temp
                previous_end = now_head
                pivot = now_head
                now_head = now_head.next

            if root == pivot:
                root = root.next
            pivot = pivot.next

        if root is None or root == pivot:
            return head
        else:
            return root


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    a = None
    for i in range(len(A)):
        n = ListNode(A[len(A) - 1 - i], a)
        a = n

    s = Solution()
    r = s.reverseKGroup(a, 4)
    print(r)
