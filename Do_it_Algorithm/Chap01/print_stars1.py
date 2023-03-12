# *를 n개 출력하되 w개마다 줄바꿈을 하는 프로그램입니다.

n = int(input("몇개를 출력할지 입력해주세요!"))
w = int(input("몇 개마다 줄바꿈을 할까요??"))

for i in range(n):
    print("*",end="")
    if (i % w == w - 1):
        print("")

if n % w:
    print()
    #마지막 줄처리? 이건 안해도 지자없는데 왜했을까?