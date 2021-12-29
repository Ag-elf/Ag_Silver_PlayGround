# -*- coding: utf-8 -*-
# @Time     : 2021/12/28 15:06
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 421_Simplify_Path.py
# @Version  : Python 3.8.5 +

class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """

    def simplifyPath(self, path: str):
        # write your code here
        result = path.split('/')
        print(result)
        path_list = []
        for k in result:
            if len(k) == 0:
                continue
            if k == "..":
                if len(path_list) != 0:
                    path_list.pop()
            elif k == ".":
                continue
            else:
                path_list.append(k)
            print(path_list, k)

        final_path = ""
        for item in path_list:
            final_path += "/" + item
        if len(final_path) == 0:
            final_path = "/"
        return final_path


if __name__ == '__main__':
    path_test = "/home/acc/./acc/../../rotk"
    s = Solution()
    res = s.simplifyPath(path_test)
    print(res)