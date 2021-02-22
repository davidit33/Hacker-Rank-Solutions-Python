# Enter your code here. Read input from STDIN. Print output to STDOUT
num_eng = int(input())
eng_est = set(map(int, input().split()))
num_french = int(input())
french_est = set(map(int, input().split()))
print(len(list(eng_est.intersection(french_est))))
