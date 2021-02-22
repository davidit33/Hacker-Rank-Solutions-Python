# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
string_size = int(input())
strig_input = input().split()
k = int(input())
string_of_k_size = itertools.combinations(''.join(strig_input), k)
count, total = 0, 0
for item in list(string_of_k_size):
    total += 1
    if 'a' in item:
        count += 1

print(count/total)



