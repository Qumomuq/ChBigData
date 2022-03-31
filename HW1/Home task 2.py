from typing import List

nums = [5, 6, 7, 1, 5, 6, 3, 8, -5, 7, -4, 3, 12, -8, 5, 11, 0, 6, 15, -13, 2, 3]
k = 3 #длина исследуемых подпоследвательностей


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:

    z = 0#переменная, для счёта
    sum_max = 0#переменная, в которую будем записывать значение наибольшей суммы

    while z <= len(nums) - k:#z меньше либо равно длине последовательности минус переменная K
        try:
            t=z
            sum_temp = 0#переменная, необходимая для временной суммы
            while t < z+k:
                sum_temp += nums[t]
                t += 1#пока мы в подпоследовательности суммируем значения и записываем в sum_temp
            if sum_temp > sum_max:
                sum_max = sum_temp#сравниваем sum_temp с sum_max
            z += 1#сдвигаемся на один элемент
        except IndexError:
            break

    return sum_max#возвращаем значение итоговой максимальной суммы


print(find_maximal_subarray_sum(nums, k))#вызываем функцию