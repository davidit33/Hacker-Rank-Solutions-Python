from itertools import permutations
string, lenght = map(str,input().split())
substrings = []
for item in list(permutations(string, int(lenght))):
    z = ''.join(item)
    substrings.append(z)
   
    
for s in sorted(substrings):
    print(s)

