n = int(input())
k = list(map(int, input().split()))
prefix_sum = [k[0]]
answer = 0

for i in range(1, n):
    prefix_sum.append(prefix_sum[i - 1] + k[i])

for i in range(n):
    answer += k[i] * (prefix_sum[n - 1] - prefix_sum[i])

print(answer % 1000000007)
