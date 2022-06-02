from typing import List


def summa(a: List[int]) -> int:
    s = 0
    for i in a:
        s += i
    return s


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    sum = 0
    i = 0
    x = len(nums) - k + 1
    array = [[0 for j in range(k)] for i in range(x)]
    while i < (len(nums) - k + 1):
        array[i] = nums[i:i + k]
        i += 1
    for i in array:
        if summa(i) >= sum:
            sum = summa(i)
    return sum

print(find_maximal_subarray_sum([1, 3, -1, 3, 5, 3, 10, 6, 7, 1, 9, 1], 3))