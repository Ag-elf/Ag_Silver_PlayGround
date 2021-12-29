# -*- coding: utf-8 -*-
# @Time     : 2021/12/29 17:35
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 472_Concatenate_Words.py
# @Version  : Python 3.8.5 +
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return

        node = self
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def dfs(self, word: str, start: int) -> bool:
        if start == len(word):
            return True
        node = self
        for i in range(start, len(word)):
            index = ord(word[i]) - ord('a')
            node = node.children[index]
            if node is None:
                return False

            if node.isEnd and self.dfs(word, i + 1):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        ans = []
        root = Trie()
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0):
                ans.append(word)
            else:
                root.insert(word)
        return ans


if __name__ == '__main__':
    s = Solution()
    raw = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    anss = s.findAllConcatenatedWordsInADict(raw)
    print(anss)
