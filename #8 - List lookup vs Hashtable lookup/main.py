import time







def timer(iterations=100):
    def decorator(fn):
        def wrapper(*a, **kwa):
            total = 0
            for _ in range(iterations):
                start = time.time()
                fn(*a, **kwa)
                end = time.time()
                total += end-start
            print(
                f"Function: {fn.__name__}",
                f"\t{iterations} iterations: {total:0.6f}s",
                f"\tper iteration: {total/iterations}s",
                sep="\n"
            )
        return wrapper
    return decorator







# option 1: List Lookup
@timer(iterations=1000)
def list_lookup(item, the_list):
    return item in the_list

# option 2: Hashtable Lookup
@timer(iterations=1000)
def hashtable_lookup(item, the_hashtable):
    try:
        the_hashtable[item]
        return True
    except Exception as ex:
        return False













list_lookup(99_999, [i for i in range(100_000)])
hashtable_lookup(99_999, {i:True for i in range(100_000)})
