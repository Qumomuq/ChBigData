from typing import List, Any
import itertools  #Воспользуемся сборником полезных итераторов

def combinations(*args: List[Any]) -> List[List]:
    a = []
    for i in itertools.product(*args):
        a.append(i)
    return a


print(combinations([1, 2], [3, 4], [5, 6]))