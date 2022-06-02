import functools


def original_info_decorator(initial_func):
    def original_info(wrap_func):
        def wrapper(*args):
            return wrap_func(*args)

        wrapper.__name__ = initial_func.__name__
        wrapper.__doc__ = initial_func.__doc__
        wrapper.__original_func = initial_func
        return wrapper

    return original_info


def print_result(func):
    @original_info_decorator(func)
    def wrapper_print(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper_print


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
