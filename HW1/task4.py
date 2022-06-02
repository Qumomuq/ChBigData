from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sums = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if i + j + k + l == 0:
                         sums += 1
    return sums

print(check_sum_of_four([1, 2, 4], [-2, -1, 3], [-1, 2, -1], [0, 2, -2]))