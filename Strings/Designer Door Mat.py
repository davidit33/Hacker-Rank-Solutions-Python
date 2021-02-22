# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split()) 

s = "WELCOME"
for i in range(1, n, 2):
    print((i * '.|.').center(m, '-'))
print (s.center(m, "-"))
for i in range(n-2, -1, -2):
    print((i * '.|.').center(m, '-'))
