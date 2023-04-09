inputNum = int(input())
count = 0
tired = []
for i in range(inputNum):

    if i % 3 == 0:
        i = i / 3
        count += 1
    if i % 2 == 0:
        count += 1
        i = i / 2
    else:
        i -= 1
        count += 1

print(count)
