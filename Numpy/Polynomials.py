import numpy as np

poli = [float(x) for x in input().split()]
x = float(input())
print(np.polyval(poli, x))