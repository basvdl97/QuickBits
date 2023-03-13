from typing import Callable
import time


def my_decorator(f:Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"Function: {f.__name__}")
        print(f"\tduration: {end-start}s")
        return result

    return wrapper


@my_decorator
def list_lookup(item, list):
    return item in list

@my_decorator
def hashtable_lookup(item, hashtable):
    try:
        hashtable[item]
        return True
    except Exception as ex:
        return False
    
result1 = list_lookup(99_999, [i for i in range(100_000)])
result2 = hashtable_lookup(99_999, {i:True for i in range(100_000)})

