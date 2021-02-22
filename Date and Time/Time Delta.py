from datetime import datetime 
import math

def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z' 
    t1_obj = datetime.strptime(t1, time_format)
    t2_obj = datetime.strptime(t2, time_format)
    return str(int(abs((t1_obj - t2_obj).total_seconds())))

num_t = int(input())
for i in range(num_t):
       t1 = input()
       t2 = input()
       print(time_delta(t1, t2)) 
