# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
num_prod = int(input())
productos = OrderedDict()

for i in range(num_prod):
    str_input = input()
    name_prod = str_input.split()[:-1] 
    price_prod = int(str_input.split()[-1]) 
    name_prod = ' '.join(name_prod) 
    if str(name_prod) in productos:
        productos[name_prod] += price_prod
    else:
        productos[name_prod] = price_prod    

for key, value in productos.items():
    print(key, value)
