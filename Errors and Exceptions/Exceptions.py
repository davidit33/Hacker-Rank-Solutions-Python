num_cases = int(input())
for i in range(num_cases):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)    
