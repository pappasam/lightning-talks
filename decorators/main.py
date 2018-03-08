'''Module demonstrating basics of Python decorators'''

import functools


def decorator_without_wraps(decorated_function):
    def inner_my_name_does_not_matter(*args, **kwargs):
        '''Decorate a function'''
        print('I have decorated your function. bahahaha')
        return decorated_function(*args, **kwargs)
    return inner_my_name_does_not_matter


def decorator_no_arguments(decorated_function):
    @functools.wraps(decorated_function)
    def inner_my_name_does_not_matter(*args, **kwargs):
        '''Decorate a function'''
        print('I have decorated your function. bahahaha')
        return decorated_function(*args, **kwargs)
    return inner_my_name_does_not_matter


def decorator_with_arguments(arg1, arg2):
    def decorator_inner(decorated_function):
        @functools.wraps(decorated_function)
        def inner_my_name_does_not_matter(*args, **kwargs):
            '''Decorate a function'''
            print(f'I have decorated your function with "{arg1}" and "{arg2}"')
            return decorated_function(*args, **kwargs)
        return inner_my_name_does_not_matter
    return decorator_inner


class DecoratorClass:

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, decorated_function):
        '''Decorate a function'''
        @functools.wraps(decorated_function)
        def inner_my_name_does_not_matter(*args, **kwargs):
            arg1, arg2 = self.arg1, self.arg2
            print(f'I have decorated your function with "{arg1}" and "{arg2}"')
            return decorated_function(*args, **kwargs)
        return inner_my_name_does_not_matter


@decorator_without_wraps
def add_numbers_lost_docstring(n1, n2):
    '''Add two numbers'''
    return n1 + n2


@decorator_no_arguments
def add_numbers_decorated(n1, n2):
    '''Add two numbers'''
    return n1 + n2


@decorator_with_arguments("hello", "world")
def add_numbers_decorated_with_args(n1, n2):
    '''Add two numbers'''
    return n1 + n2


@DecoratorClass("goodbye", "world")
def add_numbers_decorated_with_class(n1, n2):
    '''Add two numbers'''
    return n1 + n2


if __name__ == '__main__':
    print('#################################################################')
    print('# Decorator: function without arguments')
    print('#################################################################')
    print('return value:', add_numbers_decorated(1, 2))
    print('')

    print('#################################################################')
    print('# Decorator: function with arguments')
    print('#################################################################')
    print('return value:', add_numbers_decorated_with_args(1, 2))
    print('')

    print('#################################################################')
    print('# Decorator: class decorator')
    print('#################################################################')
    print('return value:', add_numbers_decorated_with_class(1, 2))
