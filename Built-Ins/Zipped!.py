import statistics
num_subjects, num_students= map(int, input().split())
scores = []
for i in range(num_students):
    scores.append(map(float, input().split())) 
for i in zip(*scores):
    print(statistics.mean(i))
