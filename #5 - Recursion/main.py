from typing import List

















def standard_sum(lst:List):
    total = 0
    for num in lst:
        total += num
    return total

def recursive_sum(lst:List):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])


'''
recersive_sum([1, 2, 3]) -> 1 + 2 + 3 + 0
                         -> 6
'''

