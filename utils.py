# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime
import time
import functools


def logger(func):
    def wrapped(*args, **kwargs):
        start_time = datetime.now().strftime('%d-%m-%Y, %H:%M')
        result = func(*args, **kwargs)
        print(f'func_name: {func.__name__} | start time: {start_time}'
              f' | args: {args} | kwargs: {kwargs} | result: {result}')

        with open('log.txt', 'a') as f:
            f.write(f'func_name: {func.__name__} | start time: {start_time}'
                    f' | args: {args} | kwargs: {kwargs} | result: {result}\n')

        return result

    return wrapped


def logger_with_file_path(file_path):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            start_time = datetime.now().strftime('%d-%m-%Y, %H:%M')
            result = func(*args, **kwargs)
            print(f'func_name: {func.__name__} | start time: {start_time}'
                  f' | args: {args} | kwargs: {kwargs} | result: {result}')

            with open(file_path, 'a') as f:
                f.write(f'func_name: {func.__name__} | start time: {start_time}'
                        f' | args: {args} | kwargs: {kwargs} | result: {result}\n')

            return result

        return wrapped
    return wrapper


def view_function_timer(prefix='', write_to=print):

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                t0 = time.time()
                return func(*args, **kwargs)
            finally:
                t1 = time.time()
                write_to(
                    'View Function',
                    '({})'.format(prefix) if prefix else '',
                    func.__name__,
                    args,
                    'Took',
                    '{:.2f}ms'.format(1000 * (t1 - t0)),
                    # args[0].build_absolute_uri(),
                )
        return inner

    return decorator


@view_function_timer()
def print_name(name):
    print('name:', name)


@logger_with_file_path(r'C:\Users\DELL\OneDrive\Документы\log.txt')
def print_age(age):
    print('age:', age)
    # return 'Возраст напечатан'


if __name__ == '__main__':
    print_name('Alex')
    print_age(35)
