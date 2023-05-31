N, X = map(int, input().split())
visit = list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
count = 0

for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + visit[i]
cnt = 0
maxvisit = []
while N >= cnt + X:
    maxvisit.append(prefix_sum[cnt+X] - prefix_sum[cnt])
    cnt += 1
if max(maxvisit) == 0:
    print("SAD")
else:
    print(max(maxvisit))
    print(maxvisit.count(max(maxvisit)))
