# 입력조건
# 첫째 줄에 N (2 <= N <= 1000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다 단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 출력 조건
# 첫쩨 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수들 정렬하기
first = data[n - 1 ] #가장 큰 수
second = data[n - 2] #두 번쨰로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k 번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0 : #m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)

