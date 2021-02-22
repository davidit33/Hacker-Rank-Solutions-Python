# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num_words = int(input())
words = []
for i in range(num_words):
    words.append(input())
c = Counter(words)
print(len(c.keys()))
print(' '.join(str(i) for i in c.values()))
