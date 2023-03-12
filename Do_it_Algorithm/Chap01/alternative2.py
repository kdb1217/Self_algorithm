# +와 -를 번갈아 출력하기2

n = int(input("몇개의 숫자를 출력할지 입력하세요"))

for _ in range(n // 2): 
    #파이썬은 무시하고 싶은 값을 언더스코어(_)로 표현할 수 있다.
    print("+-",end="")

if n % 2:
    print('+', end='')

#n이 홀수인 경우 출력? 
for _ in range(1, n // 2+1):
    print('+-', end= '')
