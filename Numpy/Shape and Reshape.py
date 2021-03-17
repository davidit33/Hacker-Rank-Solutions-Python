import numpy as np

my_array = map(int, input().split())
my_nparray = np.array([*my_array])
print(np.reshape(my_nparray,(3,3)))

#print(np.array(input().split(), int).reshape(3, 3))