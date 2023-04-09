import sys

Num = int(sys.stdin.readline())
heavyCount = 0
lightCount = 0

if Num >= 5:
    if Num - 5 == 0:
        heavyCount += 1
        print(heavyCount)
    elif Num % 3 == 0:
        lightCount = Num // 3
        print(lightCount)
    heavyCount = Num // 5
    Num = Num % 5

if Num >= 3:
    lightCount = Num // 3
    Num = Num % 3
    if Num == 0:
        print(heavyCount + lightCount)
    else:
        print(-1)
