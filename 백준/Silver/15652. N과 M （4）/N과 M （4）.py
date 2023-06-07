N, M = map(int, input().split())
answer = []
union = []


def backtracking():
    if len(answer) == M:
        if answer == sorted(answer):
            print(' '.join(map(str, answer)))
        return

    for i in range(1, N + 1):
        answer.append(i)
        backtracking()
        answer.pop()


backtracking()
