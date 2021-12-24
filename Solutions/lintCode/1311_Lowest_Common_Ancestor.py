# -*- coding: utf-8 -*-
# @Time     : 2021/12/24 15:41
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 1311_Lowest_Common_Ancestor.py
# @Version  : Python 3.8.5 +

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return f"{self.val}"


class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """

    def search(self, root, target) -> list:
        if root is None:
            return []
        elif root == target:
            return [root]
        elif root.left == target:
            return [root, root.left]
        elif root.right == target:
            return [root, root.right]
        else:
            result = []
            l_res = self.search(root.left, target)
            r_res = self.search(root.right, target)
            print(l_res, r_res)
            if len(l_res) != 0:
                result.append(root)
                result.extend(l_res)
            elif len(r_res) != 0:
                result.append(root)
                result.extend(r_res)
            return result

    def lowestCommonAncestor(self, root, p, q):
        a_list = self.search(root, p)
        b_list = self.search(root, q)
        i = 0
        print(a_list)
        print(b_list)
        while i < len(a_list) and i < len(b_list):
            if a_list[i].val != b_list[i].val:
                break
            i += 1
        i -= 1
        return a_list[i]


if __name__ == '__main__':
    root_val = [6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5]
    list_node = []
    for i in range(len(root_val)):
        if root_val[i] == -1:
            list_node.append(None)
        else:
            list_node.append(TreeNode(root_val[i]))

    for i in range(len(list_node)):
        if list_node[i] is None:
            continue
        if 2 * i + 1 >= len(list_node):
            list_node[i].left = None
        else:
            list_node[i].left = list_node[2 * i + 1]

        if 2 * i + 2 >= len(list_node):
            list_node[i].right = None
        else:
            list_node[i].right = list_node[2 * i + 2]

    s = Solution()
    res = s.lowestCommonAncestor(list_node[0], list_node[5], list_node[10])
    print(res.val)
