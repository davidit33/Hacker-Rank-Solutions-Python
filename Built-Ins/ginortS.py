# Enter your code here. Read input from STDIN. Print output to STDOUT   
s = input()

lower = []
upper = []
odd = []
even = []

for i in s:
    if i.isalpha():
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)    
    else:
        if int(i) % 2 ==  0:
            even.append(i)
        else:
            odd.append(i)
upper.sort()
lower.sort()
odd.sort()
even.sort()
s = lower + upper + odd + even
map([print(i, end = '') for i in s], s)
