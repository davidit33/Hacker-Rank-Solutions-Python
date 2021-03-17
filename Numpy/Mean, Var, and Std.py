import numpy as np


n, m = map(int, input().split())
a = np.array([input().split() for i in range(n)], int)
print(np.mean(a, axis=1))
print(np.var(a, axis=0))
print(np.around(np.std(a), 11))