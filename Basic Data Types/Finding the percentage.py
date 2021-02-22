if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    media_arr = []
    media_arr =  student_marks[query_name]
    media = 0
    for i in media_arr:
        media += i

    print(format(media / 3, '.2f'))
