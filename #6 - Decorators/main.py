











def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper


@my_decorator
def any_function_1():
    print("Hello World")


any_function_1()








