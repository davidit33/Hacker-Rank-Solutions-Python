def swap_case(s):
    new_str = ""
    for i in s:
       if i.islower():
           new_str += i.upper()
       else:
           new_str += i.lower()    

    return new_str

