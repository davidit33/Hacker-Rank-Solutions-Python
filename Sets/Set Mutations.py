# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a_num_elem = int(input())
set_a = set(map(int, input().split()))
num_of_sets = int(input())
cont = 0
my_list = []
while cont < num_of_sets:
    my_string = input()
    operation = my_string.split()[0]
    num_elem_next_set = int(my_string.split()[1])
    next_set = set(map(int, input().split()))
    command = "set_a" + "." + operation + "(" + "next_set" + ")"
    eval(command)
    cont += 1

print(sum(set_a)) 
