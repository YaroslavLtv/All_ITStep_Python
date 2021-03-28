import time


def my_decorator(func):
    def wrapper(a, b):
        print("function sum not called yet")
        response = func(a, b)
        print(f"function sum return {response}")
        return response
    return wrapper


def summ(a, b):
    return a + b


lambda_sum = lambda a, b: a +b

print(summ(1, 3))
print(lambda_sum(1, 3))

print(type(lambda_sum(4, 4)))
print(type(lambda_sum))


@my_decorator
def summ(a, b):
    return a + b

print(summ(2, 2))