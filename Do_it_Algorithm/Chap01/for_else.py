# 10 ~99 사이의 난수 b개 생성하기(13이 나오면 중단)

import random

n = int(input("난수의 갯수를 입력해주세여"))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 13:
        print("\n 13 검출")
        break
else:
    print(' \n 난수 생성을 종료합니다.')        