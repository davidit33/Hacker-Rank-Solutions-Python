from functools import lru_cache

cube = lambda x: x**3 

@lru_cache(maxsize=1000)

def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int")

    if n == 0:
        return 0    
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input())
print(list(map(cube,  map(fibonacci, range(0, num)))))