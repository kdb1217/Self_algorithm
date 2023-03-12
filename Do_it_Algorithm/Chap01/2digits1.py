#2자리 양수(10~99)입력받기

while True:
    num = int(input("두자리 정수를 입력해주세여"))
    if num >= 10 and num < 100: # 드모르간 법칙을 사용한 방법은 if not(num < 10 or num > 99):
        print(num)
        break 
    else:
         print("두자리 정수가 아닙니다. 다시입력해 주세요")
