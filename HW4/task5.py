def fizzbuzz(n: int):
    """
    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']
    >>> list(fizzbuzz(15))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    for i in range(1, n + 1):
        yield 'fizz' * (not i % 3) + 'buzz' * (not i % 5) or f'{i}'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
