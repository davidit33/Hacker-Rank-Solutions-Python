import numpy as np
n,m = map(int, input().split())
a = np.array([input().split() for i in range(n)], int)
b = np.array([input().split() for i in range(n)], int)
print(a+b)
print(a-b)
print(a*b)
print(a//b) #integer division
print(a%b)  
print(a**b)
