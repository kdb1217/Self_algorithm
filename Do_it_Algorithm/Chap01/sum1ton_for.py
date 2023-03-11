#1부터 n까지 정수의합 구하기 (for)

sum = 0
count = 1

x = int(input("정수를 입력해주세요"))

for count in range(1, x+1):
    sum += count
print(sum) 