# -*- coding: utf-8 -*-
# @Time     : 2021/4/26 13:18
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 445_Add_Two_Numbers.py
# @Version  : Python 3.8.5 +

"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_1 = []
        stack_2 = []
        r1 = l1
        r2 = l2
        while r1 is not None:
            stack_1.append(r1)
            r1 = r1.next

        while r2 is not None:
            stack_2.append(r2)
            r2 = r2.next

        next_node = None
        index = 0
        add = 0
        while True:
            index += 1
            i1 = len(stack_1) - index
            i2 = len(stack_2) - index

            if i1 < 0:
                v1 = 0
            else:
                v1 = stack_1[i1].val

            if i2 < 0:
                v2 = 0
            else:
                v2 = stack_2[i2].val

            value = (v1 + v2 + add) % 10
            add = (v1 + v2 + add) // 10

            # print(f"{value}, {add}")

            prev_node = ListNode(value)
            prev_node.next = next_node
            next_node = prev_node

            if i1 < 0 and i2 < 0:
                break
        if next_node.val == 0:
            return next_node.next
        else:
            return next_node


if __name__ == '__main__':
    list_a = [0]
    list_b = [0]

    root_a = ListNode()
    now_a = root_a
    for num in list_a:
        next_a = ListNode(val=num)
        now_a.next = next_a
        now_a = next_a

    root_b = ListNode()
    now_b = root_b
    for num in list_b:
        next_b = ListNode(val=num)
        now_b.next = next_b
        now_b = next_b

    sol = Solution()

    root = sol.addTwoNumbers(root_a.next, root_b.next)
    val_list = []
    while root is not None:
        val_list.append(root.val)
        root = root.next

    print(list_a)
    print(list_b)
    print(val_list)

