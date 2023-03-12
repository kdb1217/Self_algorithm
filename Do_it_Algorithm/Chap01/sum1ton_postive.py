# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

while True:
    n = int(input("정수를 입력해주세요"))
    if n <= 0:
        print("양수만 입력해주세요!")
    if n > 0:
        break
sum = 0
for i in range(1, n+1):
    sum += i

print(f"합은 {sum}입니다")

