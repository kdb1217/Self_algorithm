#1부터 n까지 정수의 합 구하기1(while)

n = int(input("정수를 입력하세요:"))
count = 1
sum = 0
while (count <= n):
    sum+=count
    count = count + 1

print(sum)
