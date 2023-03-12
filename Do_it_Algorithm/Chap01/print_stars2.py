# *를 n개 출력하되 w개마다 줄바꿈하기 2

n = int(input("몇개를 출력할지 입력해주세여"))
w = int(input("몇개마다 줄바꿈을 할까요?"))

for _ in range(n // w):
    print('*' *  w)

rest = n % w
if rest: # if 문 판단 1번
    print('*' * rest)