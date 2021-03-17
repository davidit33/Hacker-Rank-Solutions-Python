#https://www.sharpsightlabs.com/blog/numpy-axes-explained/
import numpy as np
n, m = map(int, input().split())
a = np.array([input().split() for i in range(n)], int)
a = np.min(a, axis=1)
print(np.max(a))
