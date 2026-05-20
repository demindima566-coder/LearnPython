def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            return storage[args]
        res = func(*args)
        storage[args] = res
        return res

    return wrapper

@cache
def my_sum(a, b):
    return a + b
#print(my_sum(2, -4))