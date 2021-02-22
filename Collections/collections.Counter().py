# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
shoes_number = int(input())
size_list = list(map(int, input().split()))
customers_number = int(input())
shoes_dict = Counter(size_list)
earned_money = 0
for i in range(0, customers_number):
    size_list, price = map(int, input().split())
    if shoes_dict[size_list] > 0:
        shoes_dict[size_list] = shoes_dict[size_list] - 1 
        earned_money += price

print(earned_money)
