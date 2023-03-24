import sys

inputAnswer = int(sys.stdin.readline())

fiboList = [0, 1]
i = 2
if inputAnswer == 0:
    print(0)
else:
    while i <= inputAnswer:
        fiboList.append(fiboList[i-1]+fiboList[i-2])
        i += 1

    print(fiboList[-1])