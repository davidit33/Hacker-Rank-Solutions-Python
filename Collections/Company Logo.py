from collections import Counter
str_input = input()
c = Counter(sorted(str_input))
for i in  c.most_common(3):
    print(*i)    

