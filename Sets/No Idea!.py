# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
x_arr = list(map(int, input().split()))
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
happines = 0
for i in x_arr:
    if i in a_set:
        happines += 1
    if i in b_set:
        happines -= 1
print(happines)
