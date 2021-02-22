if __name__ == '__main__':
    N = int(raw_input())
    my_list = []
    
    for i in range(N):
        input_string = raw_input().split()
        command = input_string[0]
        argument = input_string[1:]  
        if command != "print":
            command += "("+ ",".join(argument) +")"
            eval("my_list." + command)
        else:
            print(my_list)    
