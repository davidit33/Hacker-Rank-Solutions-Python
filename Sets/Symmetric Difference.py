m = int(input())
m_set = set(map(int,input().split()))
n = int(input())
n_set = set(map(int,input().split()))

sym_dif = []
sym_dif.append(list(m_set.difference(n_set)))
sym_dif.append(list(n_set.difference(m_set)))
new_sym_dif = []
for i in sym_dif:
    for j in i:
        new_sym_dif.append(j)    
for i in sorted(new_sym_dif):
    print(i)
