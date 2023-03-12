# 1부터 12까지 8을 건너뛰고 출력하기2

for i in list(range(1,8)) + list(range(9,13)): #출력해야하지 않는 수를 안다면 리스트에서 아예제거한다.
    print(i, end="")