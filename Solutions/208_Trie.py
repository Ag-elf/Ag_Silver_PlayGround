# -*- coding: utf-8 -*-
# @Time     : 2021/12/29 17:05
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : 208_Trie.py
# @Version  : Python 3.8.5 +

class Trie:

    def __init__(self):
        self.contents = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
        pointer = self.contents
        if not self.search(word):
            for c in word:
                if not pointer.get(c):
                    pointer[c] = {}
                pointer = pointer[c]
            pointer['END'] = {}

    def search(self, word: str) -> bool:
        pointer = self.contents
        for c in word:
            if pointer is not None:
                pointer = pointer.get(c)
            else:
                return False
        if pointer.get('END') is not None:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        pointer = self.contents
        for c in prefix:
            if pointer is not None:
                pointer = pointer.get(c)
            else:
                return False
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    print(t.search('apple'))
    print(t.startsWith('app'))
    t.insert('app')
    print(t.search('app'))
    print(t.contents)