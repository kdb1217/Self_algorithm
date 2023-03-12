# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

while True:
    width = int(input("직사각형의 넓이를 입력해주세요"))
    
    if width <= 0:
        print("넓이는 양수여야만 합니다!")
    if width > 0:
        break

for i in range(1, width+1):
    if i*i > width:
        break
    if width % i : continue # continue 문은 area가 i로 나누어 떨어지지 않으면 for문의 다음 반복으로 진행됩니다.
    print(f"{i} x {width // i}")