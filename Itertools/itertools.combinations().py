# Enter your code here. Read input from STDIN. Print output to STDOUT   
from itertools import combinations
string, num_combinations = map(str, input().split())
string = sorted(string)

for i in range(1, int(num_combinations) +1):
    list_comb = list(combinations(string, i))
    for j in list_comb:
        print (''.join(j))

