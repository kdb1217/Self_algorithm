N, M = map(int, input().split())
arr = list(map(int, input().split()))


arr = sorted(arr)
answer = []
union = []


def backtracking():
    if len(answer) == M:
        if answer == sorted(answer):
            print(' '.join(map(str, answer)))
            return

    for i in range(N):
        if arr[i] not in answer:
            answer.append(arr[i])
            backtracking()
            answer.pop()


backtracking()