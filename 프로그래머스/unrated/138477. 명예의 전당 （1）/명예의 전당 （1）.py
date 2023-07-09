def solution(k, score):
    # 풀이계획
    # k + 1만큼의 길이를 가진 리스트를 생성한다.
    # 리스트 정렬 후 첫 번째 값이 honor점수이고 answer에 추가한다. 
    # 계속 score를 추가해주고 스코어의 하나를 pop해준다.
    answer = []
    honor = []
    for i in range(len(score)):
        a = -1
        honor.append(score[i])
        honor.sort(reverse = True)
        tmp = honor[a]
        if len(honor) > k:
            a = k - 1
            tmp = honor[a]
            honor.pop()
        answer.append(tmp)
        
    return answer