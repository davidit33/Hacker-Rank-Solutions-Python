# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
num_peolple = int(input())
set_room = list(map(int, input().split()))
freq_count =  collections.Counter(set_room)
for key, value in freq_count.items():
    if value != num_peolple:
        print(key)
