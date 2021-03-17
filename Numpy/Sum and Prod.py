import numpy as np
n,m = map(int, input().split())
a = np.array([input().split() for i in range(n)], int)
c = np.sum(a, axis=0)
print(np.product(c))