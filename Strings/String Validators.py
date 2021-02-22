if __name__ == '__main__':
    s = input()
    
    line_1 = False
    line_2 = False
    line_3 = False
    line_4 = False
    line_5 = False

    for i in s:
        if line_1 != True: 
            if i.isalnum():
                line_1 = True
        if line_2 != True: 
            if i.isalpha():
                line_2 = True        
        if line_3 != True: 
            if i.isdigit():
                line_3 = True      
        if line_4 != True: 
            if i.islower():
                line_4 = True     
        if line_5 != True: 
            if i.isupper():
                line_5 = True             
    print(line_1)            
    print(line_2)            
    print(line_3)            
    print(line_4)            
    print(line_5)  
