# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(map(int, input().split()))
num_set = int(input())
cont = 0; flag = 0 
while (cont < num_set):
    set_b = set(map(int, input().split()))
    if set_b < set_a:
        flag += 1
    cont += 1
if flag == num_set:
    print("True")
else:
    print("False")    
