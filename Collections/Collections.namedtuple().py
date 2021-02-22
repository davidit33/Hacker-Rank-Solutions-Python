# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
num_students = int(input())
str_input = input().split()
students_data = namedtuple('students_data',str_input)
total = 0
for i in range(num_students):
    fields = input().split()
    students_fields = students_data(*fields) 
    total += int(students_fields.MARKS)
    
print(total/num_students)

    
