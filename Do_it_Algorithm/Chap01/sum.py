#a부터 b까지 정수의 합 구하기 (for문)

print("a부터 b까지 정수의 합을 구하자!")

a = int(input("a를 입력"))
b = int(input("b를 입력"))
temp = int
sum = 0
if (a < b):
    temp = a
    a = b
    b = temp

for i in range(b, a+1):
    sum += i

print(sum)
