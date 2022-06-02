from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(5) # Осуществляем доктест
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    >>> fizzbuzz(0)
    []
    """
    return [('fizz' * (not i % 3) + 'buzz' * (not i % 5) or f'{i}') for i in range(1, n + 1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
