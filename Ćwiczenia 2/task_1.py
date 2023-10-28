def cache_decorator(func):
    cache = {}  
    def wrapper(n):
        if n not in cache:
            result = func(n)
            cache[n] = result
        return cache[n]

    return wrapper

    def tetranacci(n):
    if n == 1 or n == 2 or n == 3:
        return 0
    elif n == 4:
        return 1
    else:
        return tetranacci(n - 1) + tetranacci(n - 2) + tetranacci(n - 3) + tetranacci(n - 4)

print(tetranacci(7))