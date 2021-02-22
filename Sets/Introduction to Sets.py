def average(array):
    # your code goes here
    total = 0
    my_set = set(array)
    for i in my_set:
        total += i
    return (total / len(my_set))

