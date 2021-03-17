import numpy as np
#print(np.zeros((3,3,3), dtype=int)) #, , row, columns
num = list(map(int, input().split())) 
#print(num) [3, 3, 3]   
print(np.zeros((num), dtype=int))
print(np.ones((num), dtype=int))
