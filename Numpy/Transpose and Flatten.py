import numpy as np
n, m = map(int, input().split())
#https://thispointer.com/numpy-insert-python/
my_array = np.array([input().split() for i in range(n)], int)
print(my_array.transpose())
print(my_array.flatten())
