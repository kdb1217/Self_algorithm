# +와-를 번갈아 출력하기1

count = int(input("몇개를 출력할지 입력해주세요"))

for i in range(count):
    if i%2 == 0:
        print("+", end='')
    else:
        print("-", end='')
    