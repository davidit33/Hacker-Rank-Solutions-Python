num_element_set = int(input())
my_set = set(map(int, input().split()))
num_command = int(input())
for i in range(num_command):
    command = input()
    if command == "pop":
        eval("my_set.pop()")
    else:
        statment = "my_set." + command.split()[0] + "(" + command.split()[1] + ")"
        eval(statment)
print(sum(list(my_set)))           
