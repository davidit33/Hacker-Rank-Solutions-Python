if __name__ == '__main__':
    dic = {}
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        dic[name] = score
        
    st_scores = dic.values()
    second = sorted(list(set(st_scores)))[1]
    second_lowest_name = []
    for key , value in dic.items():
        if value == second:
            second_lowest_name.append(key)
    second_lowest_name.sort()
    for i in second_lowest_name:
        print(i)        
        
