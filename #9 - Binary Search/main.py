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
            return total
        return wrapper
    return decorator













# option 1: Naive Search
@timer(iterations=1_000)
def naive_search(item, the_list):
    return item in the_list

# option 2: Binary Search
@timer(iterations=1_000)
def binary_search(item, the_list):
    low = 0
    high = len(the_list) - 1

    while low <= high:
        middle = low + (high - low) // 2

        if the_list[middle] == the_list:
            return middle
        elif the_list[middle] < item:
            low = middle + 1
        else:
            high = middle - 1
    return -1






d1 = naive_search(
    50_000, 
    [i for i in range(100_000)])
d2 = binary_search(
    50_000, 
    [i for i in range(100_000)])

print(f"Improvement: {100*((d1/d2)-1):.0f}%, aka {int(d1/d2)} times faster")