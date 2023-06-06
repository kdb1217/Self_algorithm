N, M = map(int, input().split())
answer = []
union = []


def backtracking():
    if len(answer) == M:
        if answer == sorted(answer):
            union.append(answer)
            print(' '.join(map(str, answer)))
            union.pop()
        return

    for i in range(1, N + 1):
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()


backtracking()
