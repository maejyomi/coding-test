def per(lst): # permutation 함수를 만들 때
    # lst가 리스트라는 전제, 반환값도 리스트

    # 선행 종료 조건
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    
    # 계산 코드
    l=[]
    for i in range(len(lst)):
        m = lst[i]
        rem_lst = list[:i] + lst[i+1:]
        for p in per(rem_lst): # 재귀함수
            l.append([m]+p)

    return l