from collections import deque
d = deque()
num_elemt = int(input())
for i in range(num_elemt):
    str_input = input()
    if len(str_input.split()) == 1: 
        command = "d" + "." + str_input + "()"
    else:
        val = str_input.split()[1]
        str_input = str_input.split()[0]
        command = "d." + str_input + "(" + val +")"
    
    eval(command)

print(' '.join(str(x) for x in d))