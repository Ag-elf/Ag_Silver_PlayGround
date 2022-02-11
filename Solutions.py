# -*- coding: utf-8 -*-
# @Time     : 2022/2/11 09:46
# @Author   : Shigure_Hotaru
# @Email    : minjie96@sencyber.cn
# @File     : solutions.py
# @Version  : Python 3.8.5 +
import math
from typing import List

"""
Q1 Cos Similarity
Basic Calculation
"""


def cos_similarity(a: List[float], b: List[float]) -> float:
    if len(a) != len(b):
        print("Vector Elements Mismatch")
        return 2.0

    sumAxB = 0.0
    sumA2 = 0.0
    sumB2 = 0.0
    for i in range(len(a)):
        sumAxB += a[i] * b[i]
        sumA2 += a[i] * a[i]
        sumB2 += b[i] * b[i]

    if sumA2 == 0 or sumB2 == 0:
        return 2.0

    else:
        return sumAxB / (math.sqrt(sumA2) * math.sqrt(sumB2))


def test_cos_similarity():
    res_1 = cos_similarity([1, 4, 0], [1, 2, 3])  # Example 1
    assert res_1 == 0.583383351196948

    res_2 = cos_similarity([1], [2])  # Example 2
    assert res_2 == 1.0

    res_3 = cos_similarity([0], [0])
    assert res_3 == 2.0


"""
Q2 Count of Atoms
Stack
"""


def print_out_atoms(count: dict) -> str:
    result = []
    for k, v in count.items():
        if v == 1:
            result.append(f"{k}")
        else:
            result.append(f"{k}{v}")

    result.sort(key=lambda x: x[0])
    return "".join(result)


def count_atoms(formula: str) -> str:
    stack = []
    result = {}
    element = ""
    count = ""
    index = 0
    while index < len(formula):

        # If get '(', push stack
        if formula[index] == '(':
            stack.append(('(', 0))
            index += 1

        # Get next atom. E.g. The O in H2O
        while index < len(formula) and formula[index].isalpha():
            if formula[index].isupper():
                if len(element) != 0:
                    break
            element += formula[index]
            index += 1

        # Get next count E.g. The 2 in H2O
        while index < len(formula) and formula[index].isdigit():
            count += formula[index]
            index += 1

        if len(element) != 0:
            if len(count) == 0:
                stack.append((element, 1))

            else:
                stack.append((element, int(count)))

        element = ""
        count = ""

        # If get ')', pop until '('
        if index < len(formula) and formula[index] == ')':
            index += 1

            # Calculate the count of the sub formula
            while index < len(formula) and formula[index].isdigit():
                count += formula[index]
                index += 1

            if len(count) == 0:
                counter = 1
            else:
                counter = int(count)

            temp = []
            while len(stack) != 0:
                atom, ct = stack.pop()
                if atom == '(':
                    break
                temp.append((atom, ct * counter))
            stack.extend(temp)

        count = ""

    while len(stack) != 0:
        atom, ct = stack.pop()
        if result.get(atom) is None:
            result[atom] = ct

        else:
            result[atom] += ct

    return print_out_atoms(result)


def test_count_atoms():
    res_1 = count_atoms("K4(ON(SO3)2)2")
    assert res_1 == "K4N2O14S4"

    res_2 = count_atoms("Mg(OH)2")
    assert res_2 == "H2MgO2"

    res_3 = count_atoms("Fe3O4")
    assert res_3 == "Fe3O4"

    res_4 = count_atoms("H2O")
    assert res_4 == "H2O"


"""
Q3 Levenshtein Distance
Dynamic Programming
"""


def levenshtein_distance(str1: str, str2: str) -> int:
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # create matrix
    matrix = [[0 for n in range(len_str1)] for k in range(len_str2)]

    # init x
    matrix[0] = [n for n in range(len_str1)]

    # init y
    for i in range(len_str2):
        matrix[i][0] = i

    for i in range(1, len_str2):
        for j in range(1, len_str1):
            if str1[j - 1] == str2[i - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1,
                               matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + cost)

    return matrix[-1][-1]


def test_levenshtein_distance():
    res_1 = levenshtein_distance("horse", "ros")
    assert res_1 == 3

    res_2 = levenshtein_distance("intention", "execution")
    assert res_2 == 5


"""
Q4 Binary Search Tree Judgement
LDR ASC
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class ValidateBST:
    def __init__(self):
        self.val = []

    def LDRWalkThrough(self, root: 'Node') -> bool:
        if root is None:
            return True

        if not self.LDRWalkThrough(root.left):
            return False

        if len(self.val) != 0 and root.val <= self.val[-1]:
            return False
        self.val.append(root.val)
        if not self.LDRWalkThrough(root.right):
            return False

        return True


def test_validate_bst():
    n1 = Node(2)
    n2 = Node(1)
    n3 = Node(3)

    n1.left = n2
    n1.right = n3

    test1 = ValidateBST()
    res_1 = test1.LDRWalkThrough(n1)
    assert res_1

    n1 = Node(5)
    n2 = Node(1)
    n3 = Node(4)
    n4 = Node(3)
    n5 = Node(6)

    n1.left = n2
    n1.right = n3

    n3.left = n4
    n3.right = n5

    test2 = ValidateBST()
    res_2 = test2.LDRWalkThrough(n1)
    assert not res_2
