# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = list(itertools.product(a, b))
print(*result, sep=" ")
