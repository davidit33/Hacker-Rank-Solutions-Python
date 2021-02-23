cube = lambda x: x**3   # complete Loading...the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    n1, n2 = 0, 1
    count = 0
    for  count in range(n):
        #print(n1)
        fib.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return fib

num = int(input())
print(list(map(cube, fibonacci(num))))