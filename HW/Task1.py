
from typing import List

A: List[int] = [-8, 8, 3, 5, 6]  # 3
B: List[int] = [7, -3, -2, -9, 6]  # -3
C: List[int] = [2, 1, 0, -9, 4]  # 0
D: List[int] = [0, 4, 5, 2, 3]  # 0


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    z = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    sum_abcd = i + j + k + l  # A[i] + B[j] + C[k] + D[l]
                    if sum_abcd == 0:
                        #  print("A: %i\tB: %i\tC: %i\tD: %i" % (i, j, k, l))
                        z += 1

    return z


print(check_sum_of_four(A, B, C, D))