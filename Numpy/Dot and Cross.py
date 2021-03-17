#https://www.mathsisfun.com/algebra/matrix-multiplying.html
#https://www.mathsisfun.com/algebra/matrix-multiplying.html
#https://www.journaldev.com/32966/numpy-matrix-multiplication
import numpy as np
n = int(input())
a = np.array([input().split() for i in range(n)], int)
b = np.array([input().split() for i in range(n)], int)
print(np.dot(a, b))
