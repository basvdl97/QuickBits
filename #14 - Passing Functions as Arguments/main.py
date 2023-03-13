

def increment(x):
    return x + 1


def apply(f, numbers):
    return [
        f(x) for x in numbers
    ]

numbers = [1, 2, 3]
print(apply(lambda x: x+1, numbers))



