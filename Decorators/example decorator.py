"""performance decorator to determine the time which the code
    takes to execute
"""
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result

    return wrapper


@performance
def time_taken():
    for i in range(1000000):
        i * 5


time_taken()
