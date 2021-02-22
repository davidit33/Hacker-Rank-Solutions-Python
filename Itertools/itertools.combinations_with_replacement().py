# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
string, num_comb = input().split(" ")
string = sorted(string)
for item in list(combinations_with_replacement(string, int(num_comb))):
    print(''.join(item))
